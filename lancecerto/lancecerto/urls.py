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
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name="index"),
	#url(r'^login/$', views.login, name="login"),
    url(r'^cadastro/$', views.cadastro, name="cadastro"),
    url(r'^produtos/$', views.produtos, name="produtos"),
    url(r'^dados_prod/$', views.dados_prod, name="dados_prod"),
    url(r'^admin/', admin.site.urls),

    url(r'^produtos_detalhes/$', views.produtos_detalhes, name="produtos_detalhes"),
    url(r'^relatoriosvendas/$', views.relatoriosvendas, name="relaoriosvendas"),
    url(r'^gerenciarvendas/$', views.gerenciarvendas, name="gerenciarvendas"),

    url(r'^contato/$', views.contato, name="contato"),
    url(r'^usuario/$', views.usuario, name="usuario"),

    url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
    url(r'^sair/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^sucesso/$', views.sucesso, name="sucesso"),

    url(r'^carrinho/$', views.carrinho, name="carrinho"),
    url(r'^compra_confirmacao/$', views.compra_confirmacao, name="compra_confirmacao"),


    url(r'^finalizar_compra/$', views.finalizar_compra, name="finalizar_compra"),
    url(r'^cadastro_produto/$', views.cadastro_produto, name="cadastro_produto"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)