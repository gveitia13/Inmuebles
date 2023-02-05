from rest_framework import serializers

from inmuebleslist_app.models import Edificacion, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comentario
        exclude = ['edificacion']
        # fields = '__all__'


class EdificacionSerializer(serializers.ModelSerializer):
    longitud_direccion = serializers.SerializerMethodField()
    comentario_set = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Edificacion
        fields = '__all__'
        # exclude = ['id']

    def get_longitud_direccion(self, object):
        cantidad_caracteres = len(object.direccion)
        return cantidad_caracteres

    def validate(self, attrs):
        if attrs['direccion'] == attrs['pais']:
            raise serializers.ValidationError("La dirección y el pais deben ser diferentes")
        else:
            return attrs

    def validate_imagen(self, attrs):
        if len(attrs) < 2:
            raise serializers.ValidationError("La url de la imagen es muy corta")
        else:
            return attrs


class EmpresaSerializer(serializers.ModelSerializer):
    edificacion_set = EdificacionSerializer(many=True, read_only=True)

    # estos son para ModelSerializer
    # edificacion_set = serializers.StringRelatedField(many=True)
    # edificacion_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # edificacion_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edificacion-details')

    class Meta:
        model = Empresa
        fields = '__all__'

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es muy corto")
#
#
# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
#
#     def update(self, instance: Inmueble, **validated_data):
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get("imagen", instance.imagen)
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, attrs):
#         if attrs['direccion'] == attrs['pais']:
#             raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
#         else:
#             return attrs
#
#     def validate_imagen(self, attrs):
#         if len(attrs) < 2:
#             raise serializers.ValidationError("La url de la imagen es muy corta")
#         else:
#             return attrs
