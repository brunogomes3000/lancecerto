# Generated by Django 2.0 on 2017-12-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171213_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='data_modificação',
        ),
    ]