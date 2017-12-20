# Generated by Django 2.0 on 2017-12-18 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido_Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pedido')),
                ('id_produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Produtos')),
            ],
        ),
    ]