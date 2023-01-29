from django.urls import path

from inmuebleslist_app.api.views import *

# from inmuebleslist_app.api.views import inmueble_list, inmueble_details

urlpatterns = [
    path('edificacion/', EdificacionListAV.as_view(), name='edificacion'),
    path('edificacion/<int:pk>/', EdificacionDetailsAV.as_view(), name='edificacion-details'),

    path('empresa/', EmpresaAV.as_view(), name='empresa'),
    path('empresa/<pk>', EmpresaDetailsAV.as_view(), name='empresa-details'),

    path('edificacion/<int:pk>/comentario/', EdificacionDetailsAV.as_view(), name='comentario-list'),
    path('edificacion/comentario/<pk>', ComentarioDetails.as_view(), name='comentario-details'),
]
