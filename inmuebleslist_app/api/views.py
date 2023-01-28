from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from inmuebleslist_app.models import Edificacion, Empresa


# @api_view(['GET', 'POST'])
# def inmueble_list(request: HttpRequest):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_details(request: HttpRequest, pk: int):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({"Error": "El inmueble no existe"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk)
#         de_serializer = InmuebleSerializer(inmueble, data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#         except Inmueble.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"Error": "El inmueble no existe"})
#         inmueble.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# APIView
class EdificacionListAV(APIView):
    def get(self, request: HttpRequest):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = EdificacionSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionDetails(APIView):
    def get(self, request: HttpRequest, pk):
        try:
            inmuebles = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'No se encuentra'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(inmuebles)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            inmuebles = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'No se encuentra'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(inmuebles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            inmuebles = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'No se encuentra'}, status=status.HTTP_404_NOT_FOUND)
        inmuebles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetailsAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada', }, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, context={'request': request})
        return Response(serializer.data,)

    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada', }, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada', }, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
