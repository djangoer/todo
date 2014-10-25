from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    url(r'^todo/', include('todoapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
