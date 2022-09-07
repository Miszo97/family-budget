from rest_framework import status
import pytest

pytestmark = pytest.mark.django_db


def test_anonymous_user_can_create_account(client):
    data = {"username": "admin", "password": "123"}
    response = client.post("/user/register/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
