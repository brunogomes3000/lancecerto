from django import forms
from django.forms import ModelForm
from .models import Usuario

class ContatoForm(forms.Form):
	nome = forms.CharField(label='Nome')
	enail = forms.EmailField(label='E-mail')
	mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

class UsuarioModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields =  ['nome', 'perfil', 'administrador', 'imagem_perfil', 'email', 'celular', 'residencial']