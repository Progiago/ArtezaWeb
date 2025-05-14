from django.db import models

# Create your models here.


class Carrinho(models.Model):
    quantidade = models.IntegerField()