# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Usuario(models.Model):
	nome = models.CharField('Nome', max_length=200)
	imagem_perfil = models.ImageField(upload_to='img/usuarios/', verbose_name='Imagem de Perfil', default='img/usuarios/noperfil.png', null=True, blank=True)
	email = models.CharField('E-mail', max_length=100)
	celular = models.CharField('Celular', max_length=11)
	residencial = models.CharField('Residêncial', max_length=11)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'


class Produtos(models.Model):
	nome = models.CharField("Nome", max_length=100)
	descricao = models.CharField("Descrição", max_length=500)
	data_inicio = models.DateField('Data de Início', null=True, blank=True)
	imagem = models.ImageField(upload_to='img/cursos/', verbose_name='Imagem', default='img/cursos/noperfil.png', null=True, blank=True)
	vagas = models.IntegerField('Vagas')
	data_criacao = models.DateField('Data de Criação', auto_now_add=True)
	data_modificacao = models.DateField('Data de Modificação', auto_now=True)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

