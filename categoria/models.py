from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome",
                            max_length=255)
    descricao = models.TextField()