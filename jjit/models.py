from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Question(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Question', null=True)
    subject = models.CharField(max_length=200)
    content = RichTextField(null=True)
    create_date = models.DateTimeField()
    like = models.IntegerField(default=0)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Answer', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    # ForeignKey(다른 모델과의 연결), on_delete=models.CASCADE는 답변에 연결된 질문 삭제되면 답변도 함께 삭제
