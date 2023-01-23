from django.urls import path

from inmuebleslist_app.api.views import *

# from inmuebleslist_app.api.views import inmueble_list, inmueble_details

urlpatterns = [
    # path('list/',inmueble_list, name='inmueble-list'),
    # path('<int:pk>/',inmueble_details, name='inmueble-details'),
    path('list/', EdificacionListAV.as_view(), name='edificacion'),
    path('<int:pk>/', EdificacionDetails.as_view(), name='edificacion-details'),

    path('empresa/', EmpresaAV.as_view(), name='empresa'),
]
