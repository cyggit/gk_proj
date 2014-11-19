__author__ = 'Administrator'

from django.db import  models
from django.contrib import admin

class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()


class user(models.Model):
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    age=models.DateField()
    gender=models.CharField(max_length=1)
    telnum=models.CharField(max_length=20)
    email=models.EmailField()

admin.site.register(BlogPost)
admin.site.register(user)