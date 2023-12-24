from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')

    class Meta:
       
        swappable = 'AUTH_USER_MODEL'
