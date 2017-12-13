# Generated by Django 2.0 on 2017-12-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('imagem', models.ImageField(blank=True, default='img/cursos/noperfil.png', null=True, upload_to='img/cursos/', verbose_name='Imagem')),
                ('vagas', models.IntegerField(verbose_name='Vagas')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('data_modificacao', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('imagem_perfil', models.ImageField(blank=True, default='img/usuarios/noperfil.png', null=True, upload_to='img/usuarios/', verbose_name='Imagem de Perfil')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('residencial', models.CharField(max_length=11, verbose_name='Residêncial')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'verbose_name': 'Usuario',
            },
        ),
    ]