__author__ = 'Administrator'
from django.template import loader,Context
from django.http import  HttpResponse
from exam.models import  BlogPost,Exam,Paper
from markdown import markdown

def archive(request):
    p = 1          #p=request.get('paperId')
    topics=Exam.objects.all()
    for topic in topics:
        topic.Question=markdown(topic.Question)
        topic.OptionA=markdown(topic.OptionA)
        topic.OptionB=markdown(topic.OptionB)
        topic.OptionC=markdown(topic.OptionC)
        topic.OptionD=markdown(topic.OptionD)
        topic.OptionE=markdown(topic.OptionE)
        topic.OptionF=markdown(topic.OptionF)
    paper=Paper.objects.get(PaperType=p)
    t=loader.get_template('test.html')
    c=Context({'topics':topics,'paper':paper})
    return HttpResponse(t.render(c))

