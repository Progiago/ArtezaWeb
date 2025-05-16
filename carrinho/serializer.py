from .models import Carrinho
from rest_framework import viewsets, serializers


# Serializers define the API representation.
class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'


# ViewSets define the view behavior.
class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
