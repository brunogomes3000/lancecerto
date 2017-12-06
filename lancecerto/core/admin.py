# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Usuario
from .models import Produtos


admin.site.register(Usuario)
admin.site.register(Produtos)
