from django.contrib import auth
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serlializers import RegistrationSerializer
from user_app.models import Account


@api_view(['GET'])
@permission_classes(IsAuthenticated)
def session_view(request):
    if request.method == 'GET':
        user = request.user
        account = Account.objects.get(email=user)
        data = {}
        if account is not None:
            data['response'] = 'El usuario esta en session'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = 'El usuario no existe'
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def logout_view(request: Request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request: Request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro del user fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            # pa token d DRF
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors

        return Response(data)


@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        account = auth.authenticate(email=email, password=password)
        if account is not None:
            data['response'] = 'El login fue exitoso'
            data['email'] = account.email
            data['username'] = account.username
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = 'Credenciales incorrectas'
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
