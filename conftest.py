import django

django.setup()

import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user(django_user_model):
    user = django_user_model.objects.create_user(username='john')
    return user


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client
