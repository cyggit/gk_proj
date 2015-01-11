#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from exam.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),
    url(r'^index',index),
    url(r'^about',about),
    url(r'^exam',exam),
    url(r'^test2',test2),
    url(r'name',get_name),
    url(r'resp',get_name_resp),
)
