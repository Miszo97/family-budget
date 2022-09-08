from budget.models import Budget
from budget.serializers import BudgetSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters


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
        return Budget.objects.filter(author=user)
