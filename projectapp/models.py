from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'


from django.db import models
# models.py

class SOUP(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class IFREN(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
        return self.project_name