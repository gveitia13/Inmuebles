from rest_framework import serializers

from inmuebleslist_app.models import Inmueble


def column_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError("La direction es muy corta")


class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(validators=[column_longitud])
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)

    def update(self, instance: Inmueble, **validated_data):
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get("imagen", instance.imagen)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, attrs):
        if attrs['direccion'] == attrs['pais']:
            raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
        else:
            return attrs

    def validate_imagen(self, attrs):
        if len(attrs) < 2:
            raise serializers.ValidationError("La url de la imagen es muy corta")
        else:
            return attrs
