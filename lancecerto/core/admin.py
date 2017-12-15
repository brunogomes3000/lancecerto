# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Usuario
from .models import Produtos
from .models import Categoria

class ProdutoAdim(admin.ModelAdmin):
	list_display =['nome','preco','data_cadastro','vendedor','quantidade']
	search_fields = ['nome', 'categoria__descricao']
	list_filter = ['data_cadastro','categoria']
		

admin.site.register(Usuario)
admin.site.register(Produtos, ProdutoAdim)
admin.site.register(Categoria)
