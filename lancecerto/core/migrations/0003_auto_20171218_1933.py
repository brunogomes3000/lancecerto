# Generated by Django 2.0 on 2017-12-18 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pedido_pedido_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Usuario'),
        ),
    ]
