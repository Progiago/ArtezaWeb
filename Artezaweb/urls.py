from django.urls import path, include
from rest_framework import routers
from usuario.serializer import UsuarioViewSet
from artezao.serializer import ArtezaoViewSet
from carrinho.serializer import CarrinhoViewSet
from produto.serializer import ProdutoViewSet
from pagamentos.serializer import PagamentoViewSet
from categoria.serializer import CategoriaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'artezao', ArtezaoViewSet)
router.register(r'pagamento', PagamentoViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'carrinho', CarrinhoViewSet)
router.register(r'categoria', CategoriaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
         
         
    ]