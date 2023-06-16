from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Q, F
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from commentapp.forms import CommentCreationForm
from django.utils import timezone
from django import forms
from django.shortcuts import get_object_or_404
from .models import Article, Category


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all())
        return form

    def form_valid(self, form):
        article = form.save(commit=False)
        article.writer = self.request.user
        article.created_at = timezone.now()
        article.category = form.cleaned_data['category']
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})




class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['created_at'] = self.object.created_at

        id = self.object.pk
        response = super().render_to_response(context)
        expire_date, now = datetime.now(), datetime.now()
        expire_date += timedelta(days=1)
        expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
        expire_date -= now
        max_age = expire_date.total_seconds()

        cookie_value = self.request.COOKIES.get('hitblog', '_')

        if f'_{id}_' not in cookie_value:
            cookie_value += f'{id}_'
            response.set_cookie('hitblog', value=cookie_value, max_age=max_age, httponly=True)
            article = self.get_object()
            article.hits = F('hits') + 1
            article.save()

        return context


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'




class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['created_at_list'] = [article.created_at for article in context['article_list']]
        context['hits_list'] = [article.hits for article in context['article_list']]
        context['category_list'] = Category.objects.all()
        category_name = self.kwargs.get('category_name')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            context['category'] = category
            context['category_description'] = category.description
        return context

    def get_queryset(self):
        article_list = super().get_queryset()
        kw = self.request.GET.get('kw', '')

        # 정렬 옵션 가져오기
        sort_by = self.request.GET.get('sort_by', '-created_at')

        category_name = self.kwargs.get('category_name', '스터디')
        if category_name == '스터디':
            # 기본 카테고리인 경우 모든 글을 가져옴
            if kw:
                article_list = article_list.filter(
                    Q(title__icontains=kw) |
                    Q(content__icontains=kw)
                ).distinct()
        else:
            # 특정 카테고리인 경우 해당 카테고리의 글만 가져옴
            category = get_object_or_404(Category, name=category_name)
            if kw:
                article_list = article_list.filter(
                    Q(title__icontains=kw) |
                    Q(content__icontains=kw),
                    category=category
                ).distinct()
            else:
                article_list = article_list.filter(category=category)

        # 정렬 기능 추가
        if sort_by == 'like':
            article_list = article_list.order_by('-like')
        elif sort_by == 'hits':
            article_list = article_list.order_by('hits')
        else:
            article_list = article_list.order_by(sort_by)

        return article_list
