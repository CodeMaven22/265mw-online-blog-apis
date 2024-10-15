from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from .models import CustomUser
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token


# Create your views here.
class CustomUserRegistration(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Create user instance

        # Create a token for the newly registered user
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'User': {
                'username': user.username,
                'employment_id': user.emp_id,
                'email': user.email,
                'token': token.key  # Return token for authentication
            },
            'Message': 'User Registered Successfully'
        }, status=status.HTTP_201_CREATED)


class CustomUserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # Get the user from validated data
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'User': {
                'username': user.username,
                'employment_id': user.emp_id,
                'email': user.email
            },
            'token': token.key
        }, status=status.HTTP_200_OK)