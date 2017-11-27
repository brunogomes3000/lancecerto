# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def galeriadeitens(request):
    return render(request, 'galeriadeitens.html')

# Create your views here.
