from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    url(r'', include('todoapp.urls')),
    url(r'^login/$','django_cas_ng.views.login',name='auth_login'),
    url(r'^logout/$','django_cas_ng.views.logout',name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
