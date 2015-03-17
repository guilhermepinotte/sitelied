from django.conf.urls import patterns, url

from contato import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)