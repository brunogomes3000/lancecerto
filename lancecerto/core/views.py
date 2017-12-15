# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Produtos
from .models import Categoria
from .forms import ContatoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect 
from django.contrib.auth.models import Group
from .forms import UsuarioModelForm

def index(request):
	produtos = Produtos.objects.all().order_by('-id')[:3]
	context = {
		'produtos': produtos

	}
	return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def relatoriosvendas(request):
    return render(request, 'RelatoriosVendas.html')

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	form2 = UsuarioModelForm(request.POST or None)
	context = {
		'form': form,
		'form2': form2
	}
	if request.method == 'POST':
		if form.is_valid():
			user_post = UserCreationForm(request.POST)
			user = user_post.save(commit=False)
			user.set_password(user_post.cleaned_data['password'])
			user.save()

			if form2.is_valid():
				usuario_post = UsuarioModelForm(request.POST)
				usuario = usuario_post.save(commit=False)
				usuario.user = user
				usuario.save()

			return redirect('/sucesso')

			grupo = Group.objects.get(name='Usuarios')
			grupo.user_set.add(user)



			#form.save()
	return render(request, 'cadastro.html', context)

def gerenciarvendas(request):
	return render(request, 'GerenciarVendas.html')

def dados_prod(request):
    return render(request, 'dados_prod.html')
# Create your views here.

def produtos(request):
	categoria = Categoria.objects.all()
	produtos = Produtos.objects.all()
	page = request.GET.get('page', 1)

	if request.method == 'GET':
		if 'nomeget' in request.GET:
			nomeget=request.GET.get("nomeget")
		else:
			nomeget=""
		if 'categoriaget' in request.GET and request.GET.get("categoriaget")!="":
			categoriaget=request.GET.get("categoriaget")
		else:
			categoriaget=Categoria.objects.values_list('id')
		produtost = Produtos.objects.filter(nome__icontains=nomeget, categoria__id__in=categoriaget).distinct()
		paginator = Paginator(produtost, 3)
	else:
		produtost = Produtos.objects.all()
		paginator = Paginator(produtost, 3)

	try: 
		produtos = paginator.page(page)
	except PageNotAnInteger:
		produtos = paginator.page(1)
	except EmptyPage:
		produtos = paginator.page(paginator.num_pages)

	context = {
		'produtos': produtos,
		'categoria': categoria,
	}
	return render(request, 'produtos.html', context)

def produtos_detalhes(request):
	id_produto = request.GET.get("id")
	produtos = Produtos.objects.get(id=id_produto)
	context = {
		'produtos': produtos
	}
	return render(request, 'produtos_detalhes.html', context)

def contato(request):
	sucesso = False
	if request.method == 'POST':
		formulario = ContatoForm(request.POST)
		if formulario.is_valid():
			nome = formulario.cleaned_data['nome']
			email = formulario.cleaned_data['email']
			mensagem = formulario.cleaned_data['mensagem']
			mensagem_completa = 'Nome:{0}\nEmail:{1}\n{2}'.format(nome, email, mensagem)
			send_mail('Contato do Site de LanceCerto', mensagem_completa, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
			sucesso = True
	else:
		formulario = ContatoForm()
	
	context = {
		'formulario': formulario,
		'sucesso': sucesso
	}
	return render(request, 'contato.html', context)

@login_required(login_url='login')
def usuario(request):
	return render(request, 'usuario.html')

def sucesso(request):
	return render(request, 'sucesso.html')