from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import DetailView
from subscribeapp.models import Subscription
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article




has_ownership = [login_required, account_ownership_required]


# Create your views here.


class AccountCreateView(CreateView):
    # 장고에서 제공하는 기본 모델
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    # reverse_lazy는 클래스에서
    template_name = 'accountapp/create.html'
    # 어느 html파일로 갈지




class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())

        subscription_list = Subscription.objects.filter(user=self.get_object())
        projects = subscription_list.values_list('project', flat=True)
        subscription_articles = Article.objects.filter(project__in=projects)

        context = super().get_context_data(object_list=object_list, **kwargs)
        context['subscription_list'] = subscription_list
        context['subscription_articles'] = subscription_articles
        return context



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    # 장고에서 제공하는 기본 모델
    model = User
    context_object_name = 'target_user'
    # 장고에서 제공하는 html
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    # reverse_lazy는 클래스에서
    template_name = 'accountapp/update.html'

    # 어느 html파일로 갈지


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # 자바스크립트 confirm 메시지를 띄우고 확인 버튼을 누르면 삭제 수행
        confirm_message = "회원탈퇴를 진행하시겠습니까?"
        if request.POST.get('confirm_message') == confirm_message:
            self.object.delete()
            return HttpResponse("회원탈퇴가 완료되었습니다.")
        else:
            return render(request, self.template_name, {'target_user': self.object})'''


