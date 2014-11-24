from django.conf.urls import patterns, include, url
from django.contrib import admin
from exam.views import archive,index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),
    url(r'^index',index),#TODO:BOOTSTRAP css ,有问题，连首页都显示不正常。
)
