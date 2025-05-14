from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Artezao(AbstractBaseUser):
    usuario = models.CharField(verbose_name="Usuario", max_length=50)
    genero = models.CharField(verbose_name="Genero", max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=254)
    nome_fantasia = models.CharField(verbose_name="Nome Fantasia",
                                     max_length=255)
    cpnj = models.CharField(verbose_name='CNPJ',
                            max_length=10)
    data_de_nascimento = models.DateField(verbose_name="Data de Nascimento",
                                          auto_now=False, auto_now_add=False)
    pais = models.CharField(verbose_name="Pais", max_length=50)
    cidade = models.CharField(verbose_name="Cidade", max_length=50)
    cep = models.CharField(verbose_name='CEP', max_length=30)
    endereco = models.CharField(verbose_name='Endereço', max_length=255)
    