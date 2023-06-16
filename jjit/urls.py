#awesite/jjit/urls.py

from django.urls import path
from . import views

app_name = 'jjit' # 앱 이름 정의

urlpatterns = [
    path('', views.index, name='index'), # 'index'라는 이름으로 URL 패턴에 이름 부여
    path('<int:question_id>/', views.detail, name='detail'), # 'detail'이라는 이름으로 URL 패턴에 이름 부여
    path('<int:question_id>/answer/create/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),#질문 추가 버튼
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),


    # 'answer_create'라는 이름으로 URL 패턴에 이름 부여,#93
]
