from django.db import models
from carrinho.models import Carrinho
from categoria.models import Categoria
# Create your models here.


class Produto(models.Model):
    nome = models.CharField(verbose_name=("nome"), max_length=50)
    descricao = models.TextField(verbose_name=(""))
    img = models.ImageField(verbose_name=("imagen"), upload_to=None,
                            height_field=None, width_field=None, 
                            max_length=None)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    produto_fk = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    categoria = models.OneToOneField(Categoria,
                                     on_delete=models.CASCADE,
                                     primary_key=True)