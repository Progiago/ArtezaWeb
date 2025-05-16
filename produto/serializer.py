from .models import Produto
from rest_framework import viewsets, serializers


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model """

    class Meta:
        """ ProductSerializer's Meta class """

        model = Produto
        filds = '__all__'
        

# ViewSets define the view behavior.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer
