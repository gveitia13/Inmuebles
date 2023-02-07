from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    avg = models.FloatField(default=0)
    number_calification = models.IntegerField(default=0)
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


class Comentario(models.Model):
    comentario_user = models.ForeignKey(User, on_delete=models.CASCADE)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, )
    calificacion = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.calificacion} {self.edificacion.direccion}'
