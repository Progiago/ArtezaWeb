# Generated by Django 5.2.1 on 2025-05-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_forma_de_pagamento', models.CharField(max_length=255, verbose_name='forma de pagar')),
                ('data_da_compra', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=255, verbose_name='descrição')),
            ],
        ),
    ]
