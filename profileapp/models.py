from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # on_delete는 유저객체가 사라지면, 그와 연결된 프로필객체가 사라지는 것
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 프로필 사진, 이미지 파일 서버에 저장 /media/profile에 저장
    image = models.ImageField(upload_to='profile/', null=True)
    #닉네임 unique 하나만 유일하게
    nickname = models.CharField(max_length=20, unique=True, null=True)
    #대화명
    message = models.CharField(max_length=100, null=True)
