from django.conf.urls import patterns, url

from servicos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)