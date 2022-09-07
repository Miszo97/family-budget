from rest_framework import status
import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


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


def test_user_can_create_budget(api_client, django_user_model, user):
    shared_account = django_user_model.objects.create_user(username='ala')
    data = {"name": "admin", "author": user.pk, "shared_account": [shared_account.pk], "income": 1000,
            "expenses": [{"amount": 100, "category": "HOME"}]}
    response = api_client.post("/user/me/budget/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
