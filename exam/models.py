#-*-coding:utf-8-*-
__author__ = 'Administrator'

from django.db import  models
from django.contrib import admin

class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    Catagory=models.SmallIntegerField()
    body=models.TextField()
    timestamp=models.DateTimeField()

#
class User(models.Model):
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    age=models.DateField()
    gender=models.CharField(max_length=1)
    telnum=models.CharField(max_length=20)
    email=models.EmailField()


class Exam(models.Model):
    TopicId=models.AutoField(primary_key=True)  #题目ID
    PaperId=models.IntegerField()               #对应的试卷
    PaperNo=models.SmallIntegerField()          #在试卷中的题号
    QuestionType=models.IntegerField()          #题目类型，1单选、2多选、3判断,4资料分析
    QuestionSet=models.SmallIntegerField(blank=True)      #多选题集合，与PaperId一起组成键
    Material=models.TextField(blank=True)       #该题有资料的，先显示资料
    Question=models.TextField()                 #问题
    OptionA=models.TextField()                  #选项A,B,C,D,E,F
    OptionB=models.TextField()
    OptionC=models.TextField(blank=True)
    OptionD=models.TextField(blank=True)
    OptionE=models.TextField(blank=True)
    OptionF=models.TextField(blank=True)
    Answer=models.CharField(max_length=10)
    Suggestion=models.TextField()
    def __unicode__(self):
        return repr(self.TopicId)

# class ExamAdmin(admin.ModelAdmin):

# ---------------------------------------------------------------------------------------------
class Paper(models.Model):
    PaperId=models.AutoField(primary_key=True)      #试卷ID
    PaperType=models.CharField(max_length=10)       #试卷类型，1公务员，2职员，3雇员，4临聘
    Year=models.CharField(max_length=10)            #是哪一年的试卷
    YearGap=models.CharField(max_length=10)         #上半年还是下半年，1=上半年，2=下半年
    Dirstrict=models.CharField(max_length=20)       #哪个地区的试题，将来换成级联菜单
    Title=models.CharField(max_length=100)          #试卷标题
    Notice=models.TextField(blank=True)                       #试卷前的注意事项
    Part1Title=models.TextField(max_length=100,blank=True)     #第一部分标题
    Part1Sum=models.SmallIntegerField(blank=True)                        #第一部分有几题
    Part2Title=models.TextField(max_length=100,blank=True)     #第二部分标题
    Part2Sum=models.SmallIntegerField(blank=True)                        #第二部分从第几题开始
    Part3Title=models.TextField(max_length=100,blank=True)     #第三部分标题
    Part3Sum=models.SmallIntegerField(blank=True)                        #第三部分从第几题开始
    Part4Title=models.TextField(max_length=100,blank=True)     #第四部分标题
    Part4Sum=models.SmallIntegerField(blank=True)                        #第四部分从第几题开始
    Part5Title=models.TextField(max_length=100,blank=True)     #第五部分标题
    Part5Sum=models.SmallIntegerField(blank=True)                        #第五部分从第几题开始
    Part6Title=models.TextField(max_length=100,blank=True)     #第六部分标题
    Part6Sum=models.SmallIntegerField(blank=True)                        #第六部分从第几题开始
    def __unicode__(self):
        return repr(self.PaperId)

admin.site.register(BlogPost)
admin.site.register(User)
admin.site.register(Exam)
admin.site.register(Paper)