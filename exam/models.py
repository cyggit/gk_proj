#-*-coding:utf-8-*-
__author__ = 'Administrator'

from django.db import  models
from django.contrib import admin

class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()


class Users(models.Model):
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    age=models.DateField()
    gender=models.CharField(max_length=1)
    telnum=models.CharField(max_length=20)
    email=models.EmailField()


class Exam(models.Model):
    TopicId=models.AutoField(primary_key=True)  #题目ID
    PaperId=models.IntegerField()               #对应的试卷
    QuestionType=models.IntegerField()          #题目类型，单选、多选、判断
    Question=models.TextField()                 #问题
    OptionA=models.TextField()                  #选项A,B,C,D,E,F
    OptionB=models.TextField()
    OptionC=models.TextField(blank=True)
    OptionD=models.TextField(blank=True)
    OptionE=models.TextField(blank=True)
    OptionF=models.TextField(blank=True)
    Answer=models.CharField(max_length=10)
    Suggestion=models.TextField()


admin.site.register(BlogPost)
admin.site.register(Users)
admin.site.register(Exam)