from .models import Artezao
from rest_framework import viewsets, serializers


# Serializers define the API representation.
class ArtezaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artezao
        fields = '__all__'


# ViewSets define the view behavior.
class ArtezaoViewSet(viewsets.ModelViewSet):
    queryset = Artezao.objects.all()
    serializer_class = ArtezaoSerializer
