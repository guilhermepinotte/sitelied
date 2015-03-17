from django.conf.urls import patterns, url

from publicacoes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)