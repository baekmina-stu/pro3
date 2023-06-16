
from django.contrib import admin
from .models import Question #현재 디렉토리에서 Question의 models 모듈을 가져온다

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    #Question 모델의 관리자(admin) 페이지에서의 동작을 커스터마이징하기 위해 QuestionAdmin 클래스를 선언
    # serch_feild에 subject 추가

admin.site.register(Question, QuestionAdmin)

#장고에서 모델 Question 관리하기
# QuestionAdmin 클래스를 추가하고