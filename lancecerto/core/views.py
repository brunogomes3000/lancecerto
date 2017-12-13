# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Produtos

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def relatoriosvendas(request):
    return render(request, 'relatoriosvendas.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def GerenciarVendas(request):
	return render(request, 'GerenciarVendas.html')

def produtos(request):
    return render(request, 'produtos.html')

def dados_prod(request):
    return render(request, 'dados_prod.html')
# Create your views here.

def produtos(request):
	produtos = Produtos.objects.all()
	context = {
		'produtos': produtos
	}
	return render(request, 'produtos.html', context)

def produtos_detalhes(request):
	id_produto = request.GET.get("id")
	produto = Produtos.objects.get(id=id_produto)
	context = {
		'produto': produto
	}
	return render(request, 'produtos_detalhes.html', context)
