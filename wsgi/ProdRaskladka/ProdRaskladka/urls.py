from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.IndexView.as_view(), name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^generate$', 'ProdRaskladka.views.generate', name='generate'),
                       url(r'^delete$', 'ProdRaskladka.views.delete', name='delete'),
                       )
