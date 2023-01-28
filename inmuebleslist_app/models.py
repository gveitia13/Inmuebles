from django.db import models


class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey('inmuebleslist_app.Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion


class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    web_site = models.URLField(max_length=252)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
