from rest_framework import status
import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_anonymous_user_can_create_account(api_client):
    data = {"username": "admin", "password": "123"}
    response = api_client.post(reverse("register"), data=data)
    assert response.status_code == status.HTTP_201_CREATED
