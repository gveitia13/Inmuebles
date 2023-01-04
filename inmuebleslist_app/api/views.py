from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inmuebleslist_app.api.serializers import InmuebleSerializer
from inmuebleslist_app.models import Inmueble


@api_view(['GET', 'POST'])
def inmueble_list(request: HttpRequest):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        de_serializer = InmuebleSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_details(request: HttpRequest, pk: int):
    if request.method == 'GET':
        inmueble = Inmueble.objects.get(pk=pk)
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=pk)
        de_serializer = InmuebleSerializer(inmueble, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)
    if request.method == 'DELETE':
        inmueble = Inmueble.objects.get(pk=pk)
        inmueble.delete()
        data = {
            'result': True
        }
        return Response(data)
