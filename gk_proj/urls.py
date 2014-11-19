from django.conf.urls import patterns, include, url
from django.contrib import admin
from gk_proj.views import archive

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gk_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', archive),
)
