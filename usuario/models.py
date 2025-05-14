from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from time import timezone
from .manager import CustomUserManager
# Create your models here.


class Usuario(AbstractBaseUser):
    GENERO_CHOICES = {
        "HOMEN": 'Homen',
        "MULHER": 'Mulher',
        "NAO_BINARIO": 'Não-binario',
        "SEM_RESPOSTA": 'sem/resposta'
    }
    
    usuario = models.CharField(verbose_name="usuario", max_length=255)
    email = models.EmailField(verbose_name="email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone)
    genero = models.CharField(verbose_name="genero", choices=GENERO_CHOICES,
                              max_length=20) 
    nome = models.CharField(verbose_name="nome", max_length=50)
    cpf = models.CharField(verbose_name="CPF", max_length=10)
    data_de_nascimento = models.DateField()
    pais = models.CharField(verbose_name="PAIS", max_length=50)
    cidade = models.CharField(verbose_name="CIDADE", max_length=50)
    cep = models.CharField(verbose_name="CEP", max_length=30)
    endereco = models.CharField(verbose_name="Endereço", max_length=60)
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email
    