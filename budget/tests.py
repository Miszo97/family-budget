from rest_framework import status
import pytest
from budget.enums import ExpenseCategory
from budget.models import Budget
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_user_can_create_budget(api_client, django_user_model, user):
    shared_account_1 = django_user_model.objects.create_user(username='ala')
    shared_account_2 = django_user_model.objects.create_user(username='ola')
    data = {"name": "admin", "author": user.pk, "shared_accounts": [shared_account_1.pk, shared_account_2.pk],
            "income": 1000,
            "expenses": [{"amount": 100, "category": ExpenseCategory.EDUCATION}]}
    response = api_client.post(reverse("budgets-list"), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


def test_user_can_get_their_budgets(api_client, user):
    Budget.objects.create(name="Hawaii", author=user, income=1000)
    Budget.objects.create(name="Sydney", author=user, income=1000)

    response = api_client.get(reverse("budgets-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 2


def test_user_can_filter_their_budgets(api_client, user):
    Budget.objects.create(name="Hawaii", author=user, income=1000)
    Budget.objects.create(name="Sydney", author=user, income=1000)

    response = api_client.get(reverse("budgets-list"), {"name": "Hawaii"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1


def test_user_cannot_get_other_user_budgets(api_client, django_user_model):
    ola_user = django_user_model.objects.create_user(username='Ola')
    Budget.objects.create(name="Hawaii", author=ola_user, income=1000)

    response = api_client.get(reverse("budgets-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 0


def test_user_can_get_budgets_he_share(api_client, django_user_model, user):
    ola_user = django_user_model.objects.create_user(username='Ola')
    budget = Budget.objects.create(name="Hawaii", author=ola_user, income=1000)
    budget.shared_accounts.add(user)
    response = api_client.get(reverse("shared-budgets-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1


def test_user_cannot_share_budget_with_him_self(api_client, user):
    data = {"name": "admin", "author": user.pk, "shared_accounts": [user.pk],
            "income": 1000,
            "expenses": [{"amount": 100, "category": ExpenseCategory.EDUCATION}]}
    response = api_client.post(reverse("budgets-list"), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

