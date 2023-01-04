from django.urls import path

from inmuebleslist_app.api.views import *

# from inmuebleslist_app.api.views import inmueble_list, inmueble_details

urlpatterns = [
    # path('list/',inmueble_list, name='inmueble-list'),
    # path('<int:pk>/',inmueble_details, name='inmueble-details'),
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>/', InmuebleDetails.as_view(), name='inmueble-details'),
]

