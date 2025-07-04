# Generated by Django 5.2.1 on 2025-05-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artezao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('genero', models.CharField(max_length=50, verbose_name='Genero')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('nome_fantasia', models.CharField(max_length=255, verbose_name='Nome Fantasia')),
                ('cpnj', models.CharField(max_length=10, verbose_name='CNPJ')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=30, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
