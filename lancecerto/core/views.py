# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def relatoriosvendas(request):
    return render(request, 'relatoriosvendas.html')

def cadastro(request):
    return render(request, 'cadastro.html')

<<<<<<< HEAD
def GerenciarVendas(request):
	return render(request, 'GerenciarVendas.html')
=======
<<<<<<< HEAD
def produtos(request):
    return render(request, 'produtos.html')

def dados_prod(request):
    return render(request, 'dados_prod.html')

=======
>>>>>>> 1107f6fb4eafe494cbcdc27394c375f621765bb2

>>>>>>> 7cb216170485b95e8dce1b59234e5ebf360a1a30
# Create your views here.
