# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	cpf = models.CharField('CPF', primary_key=True, max_length=11)
	nome = models.CharField('Nome', max_length=200)
	administrador = models.BooleanField('ADM')
	perfil = models.CharField('Perfil', max_length=500)
	imagem_perfil = models.ImageField(upload_to='img/usuarios/', verbose_name='Imagem de Perfil', default='img/usuarios/noperfil.png', null=True, blank=True)
	email = models.CharField('E-mail', max_length=100)
	celular = models.CharField('Celular', max_length=11)
	senha = models.CharField('senha', max_length=100)
	residencial = models.CharField('Residêncial', max_length=11)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
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
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

class Produtos(models.Model):
	nome = models.CharField("Nome", max_length=100)
	descricao = models.CharField('Descrição', max_length=500)
	preco = models.CharField('Preço', max_length=50, null=True)
	imagem = models.ImageField(upload_to='static/img/', verbose_name='Imagem Produto', default='static/img/noperfil.png', null=True, blank=True)
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

class Pedido(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
	data_criacao = models.DateField('Data de Criação', auto_now_add=True)

class Pedido_Produto(models.Model):
	id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True)
	id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

