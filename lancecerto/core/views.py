# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def relatoriosvendas(request):
    return render(request, 'relatoriosvendas.html')

# Create your views here.
