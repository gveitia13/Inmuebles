from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inmuebleslist_app.api.views import *

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

urlpatterns = [
    path('edificacion/', EdificacionListAV.as_view(), name='edificacion'),
    path('edificacion/<int:pk>/', EdificacionDetailsAV.as_view(), name='edificacion-details'),
    path('', include(router.urls)),

    # path('empresa/', EmpresaAV.as_view(), name='empresa'),
    # path('empresa/<pk>', EmpresaDetailsAV.as_view(), name='empresa-details'),

    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<pk>', ComentarioDetails.as_view(), name='comentario-details'),
]
