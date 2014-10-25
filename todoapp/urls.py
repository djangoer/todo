from django.conf.urls import patterns, include, url

urlpatterns = patterns('todoapp.views',
	url(r'^$', 'home', name='home'),
	url(r'^calendar/$', 'calendar', name='calendar'),
)