from django.urls import reverse

from budget.models import Budget
from budget.serializers import BudgetSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters


def get_core_url(url: str) -> str:
    question_mark = url.find("?")
    if question_mark > 0:
        return url[:question_mark]
    return url


class BudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing budgets.
    """

    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name",)

    def get_queryset(self):
        user = self.request.user
        url = self.request.get_full_path()
        if get_core_url(url) == reverse('budgets-list'):
            return Budget.objects.filter(author=user)
        elif get_core_url(url) == reverse('shared-budgets-list'):
            return self.request.user.shared_budgets.all()
