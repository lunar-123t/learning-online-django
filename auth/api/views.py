from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework.views import APIView

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


