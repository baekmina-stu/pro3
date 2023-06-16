from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_decorator
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

from articleapp.models import Article  # 추가

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        # user의 pk를 detail에 넘겨준다.
        # 하는 이유 프로필 생성후 유저 detail.html로 가기 위해서


@method_decorator(profile_decorator, 'get')
@method_decorator(profile_decorator, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        # user의 pk를 detail에 넘겨준다.
        # 하는 이유 프로필 생성후 유저 detail.html로 가기 위해서

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_list = Article.objects.order_by('-created_at')[:12]  # article_list를 12개까지 제한
        context['project_list'] = project_list
        return context


