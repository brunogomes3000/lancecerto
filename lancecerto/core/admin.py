# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Usuario
from .models import Produtos
from .models import Categoria

admin.site.register(Usuario)
admin.site.register(Produtos)
admin.site.register(Categoria)
