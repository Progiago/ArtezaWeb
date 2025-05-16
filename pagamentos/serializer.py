from .models import Pagamento
from rest_framework import viewsets, serializers


# Serializers define the API representation.
class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'


# ViewSets define the view behavior.
class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
