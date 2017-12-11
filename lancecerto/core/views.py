# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def relatoriosvendas(request):
    return render(request, 'RelatoriosVendas.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def gerenciarvendas(request):

def GerenciarVendas(request):
	return render(request, 'GerenciarVendas.html')

def produtos(request):
    return render(request, 'produtos.html')

def dados_prod(request):
    return render(request, 'dados_prod.html')
# Create your views here.