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
def produtos(request):
    return render(request, 'produtos.html')

def dados_prod(request):
    return render(request, 'dados_prod.html')

=======
>>>>>>> 1107f6fb4eafe494cbcdc27394c375f621765bb2

# Create your views here.
