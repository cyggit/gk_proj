__author__ = 'Administrator'
from django.template import loader,Context
from django.http import  HttpResponse
from gk_proj.models import  BlogPost

def archive(request):
    posts=BlogPost.objects.all()
    t=loader.get_template('test.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))