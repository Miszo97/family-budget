from django.urls import reverse
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from budget.models import Budget
from budget.serializers import BudgetSerializer
from utils import get_core_url


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
