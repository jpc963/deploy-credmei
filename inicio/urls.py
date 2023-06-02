from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'ceps', CepViewSet)

urlpatterns = [
    path('routes', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', buscar_cep, name='buscar_cep'),
    path('historico', historico, name='historico'),
]
