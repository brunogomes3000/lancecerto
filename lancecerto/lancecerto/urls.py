"""lancecerto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.login, name="login"),
    url(r'^cadastro/$', views.cadastro, name="cadastro"),
    url(r'^produtos/$', views.produtos, name="produtos"),
    url(r'^dados_prod/$', views.dados_prod, name="dados_prod"),
    url(r'^admin/', admin.site.urls),

    url(r'^produtos_detalhes/$', views.produtos_detalhes, name="produtos_detalhes"),
    url(r'^relatoriosvendas/$', views.relatoriosvendas, name="relaoriosvendas"),
    url(r'^gerenciarvendas/$', views.gerenciarvendas, name="gerenciarvendas"),
    
]
