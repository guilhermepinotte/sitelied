from django.conf.urls import patterns, url

from projetos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)