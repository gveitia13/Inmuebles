from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inmuebleslist_app.api.views import *

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

urlpatterns = [
    path('edificacion/', EdificacionAV.as_view(), name='edificacion'),
    path('edificacion/list/', EdificacionList.as_view(), name='edificacion-list'),
    path('edificacion/<int:pk>/', EdificacionDetailsAV.as_view(), name='edificacion-details'),
    path('', include(router.urls)),
    # path('empresa/', EmpresaAV.as_view(), name='empresa'),
    # path('empresa/<pk>', EmpresaDetailsAV.as_view(), name='empresa-details'),

    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<pk>/', ComentarioDetails.as_view(), name='comentario-details'),
    # path('edificacion/comentarios/<str:username>/', UsuarioComentario.as_view(), name='usuario-comentario-details'),
    path('edificacion/comentarios/', UsuarioComentario.as_view(), name='usuario-comentario-details'),
]
