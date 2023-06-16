from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from projectapp.models import Project
from django.urls import reverse

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(blank=True, null=True)  # 수정된 부분
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    hits = models.PositiveIntegerField(default=1, verbose_name='조회수')