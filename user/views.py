# Create your views here.
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
