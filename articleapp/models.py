from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from projectapp.models import Project
from django.urls import reverse


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='article', null=True)  # 수정된 부분
    title = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    hits = models.PositiveIntegerField(default=1, verbose_name='조회수')


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article:list', kwargs={'category_name': self.name})  # 수정된 부분
