from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('inmuebleslist_app.api.urls')),
]
