from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

class chatgptcbot(models.Model):
    texttest = models.CharField(max_length=255, null=False)



class ChatGptBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messageInput = models.TextField()
    bot_response = models.TextField()
    def __str__(self):
        return self.user.username

