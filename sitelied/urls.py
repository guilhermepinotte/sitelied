from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitelied.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('home.urls', namespace="home")),
    url(r'^contato/', include('contato.urls', namespace="contato")),
    url(r'^projetos/', include('projetos.urls', namespace="projetos")),
    url(r'^publicacoes/', include('publicacoes.urls', namespace="publicacoes")),
    url(r'^servicos/', include('servicos.urls', namespace="servicos")),
    url(r'^sobre/', include('sobre.urls', namespace="sobre")),
    url(r'^admin/', include(admin.site.urls)),    
)
