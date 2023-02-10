from django.contrib.auth.models import User
from rest_framework import serializers

from user_app.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise serializers.ValidationError({'error': 'El password de confirmación no coincide'})
        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'El email ya existe'})

        # account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account = Account.objects.create(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            phone_number=self.validated_data['phone_number']
        )
        account.set_password(self.validated_data['password'])
        # account.set_password(password)
        account.save()
        return account
