from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'emp_id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        # Create user instance
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            emp_id=validated_data['emp_id']
        )
        return user  # Return the user instance for further processing in the view


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError(_('Email and password must be provided.'))

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(_('Invalid credentials.'))

        if not user.is_active:
            raise serializers.ValidationError(_('User account is disabled.'))

        return {'user': user}
