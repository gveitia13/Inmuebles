from rest_framework import serializers

from inmuebleslist_app.models import Inmueble


class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)

    def update(self, instance:Inmueble, validated_data):
        instance.pais = validated_data['pais']
        instance.descripcion = validated_data['descripcion']
        instance.imagen = validated_data['image']
        instance.direccion = validated_data['direccion']
        instance.active = validated_data['active']
        instance.save()

