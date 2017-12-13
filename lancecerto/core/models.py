# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Usuario(models.Model):
	cpf = models.CharField('CPF', primary_key=True, max_length=11)
	nome = models.CharField('Nome', max_length=200)
	administrador = models.BooleanField('ADM')
	imagem_perfil = models.ImageField(upload_to='img/usuarios/', verbose_name='Imagem de Perfil', default='img/usuarios/noperfil.png', null=True, blank=True)
	email = models.CharField('E-mail', max_length=100)
	celular = models.CharField('Celular', max_length=11)
	senha = models.CharField('senha', max_length=100)
	residencial = models.CharField('Residêncial', max_length=11)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

class Categoria(models.Model):
	descricao = models.CharField("Nome", max_length=100)
	def __str__(self):
		return self.descricao
	class Meta:
		verbose_name = 'Categorias'
		verbose_name_plural = 'Categorias'

class Produtos(models.Model):
	nome = models.CharField("Nome", max_length=100)
	descricao = models.CharField('Descrição', max_length=500)
	preco = models.CharField('Preço', max_length=50, null=True)
	imagem = models.ImageField(upload_to='static/img/', verbose_name='Imagem', default='static/img/noperfil.png', null=True, blank=True)
	quantidade = models.IntegerField('Quantidade', null=True)
	data_cadastro = models.DateField('Data de Cadastro', auto_now_add=True)
	data_modificacao = models.DateField('Data de Modificação', auto_now=True)
	vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
	categoria = models.ManyToManyField(Categoria)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

