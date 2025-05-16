from django.db import models

# Create your models here.

class Pagamento(models.Model):
    nome_da_forma_de_pagamento = models.CharField(verbose_name="forma de pagar",
                                                  max_length=255)
    data_da_compra = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(verbose_name="descrição", max_length=255)
    