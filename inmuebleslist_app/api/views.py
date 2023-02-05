from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from inmuebleslist_app.api.permissions import AdminOrReadOnly, ComentarioUserOrReadOnly
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from inmuebleslist_app.models import Edificacion, Empresa, Comentario


# APIView

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

class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        edificacion = Edificacion.objects.get(pk=pk)

        if not self.request.user.is_authenticated:
            raise ValidationError('inicie session')
        user: User = self.request.user

        comentario_queryset = Comentario.objects.filter(edificacion=edificacion, comentario_user=user)
        if comentario_queryset.exists():
            raise ValidationError('El user ya escribió un comentario para este inmueble')

        serializer.save(edificacion=edificacion, comentario_user=user)


class ComentarioList(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion_id=pk)


class ComentarioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [ComentarioUserOrReadOnly, ]


# class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ComentarioDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


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


class EdificacionDetailsAV(APIView):
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


class EmpresaVS(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [AdminOrReadOnly]


# class EmpresaVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Empresa.objects.all()
#         serializer = EmpresaSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Empresa.objects.all()
#         edificacion_set = get_object_or_404(queryset, pk=pk)
#         serializer = EmpresaSerializer(edificacion_set)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = EmpresaSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = EmpresaSerializer(empresa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
#         empresa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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
        return Response(serializer.data, )

    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada', }, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada', }, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
