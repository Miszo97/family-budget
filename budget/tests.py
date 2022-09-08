from rest_framework import status
import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from budget.enums import ExpenseCategory
from budget.models import Budget
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_user_can_create_budget(api_client, django_user_model, user):
    shared_account_1 = django_user_model.objects.create_user(username='ala')
    shared_account_2 = django_user_model.objects.create_user(username='ola')
    data = {"name": "admin", "author": user.pk, "shared_account": [shared_account_1.pk, shared_account_2.pk], "income": 1000,
            "expenses": [{"amount": 100, "category": ExpenseCategory.EDUCATION}]}
    response = api_client.post(reverse("budgets-list"), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

def test_user_can_get_their_budgets(api_client, user):
    budget_1 = Budget.objects.create(name="Hawaii", author=user, income=1000)
    budget_2 = Budget.objects.create(name="Sydney", author=user, income=1000)

    response = api_client.get(reverse("budgets-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

def test_user_can_filter_their_budgets(api_client, user):
    budget_1 = Budget.objects.create(name="Hawaii", author=user, income=1000)
    budget_2 = Budget.objects.create(name="Sydney", author=user, income=1000)

    response = api_client.get(reverse("budgets-list"), {"name": "Hawaii"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

def test_user_cannot_get_other_user_budgets(api_client, django_user_model):
    ola_user = django_user_model.objects.create_user(username='Ola')
    budget = Budget.objects.create(name="Hawaii", author=ola_user, income=1000)

    response = api_client.get(reverse("budgets-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0