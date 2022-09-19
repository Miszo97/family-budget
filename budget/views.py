from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from budget.models import Budget
from budget.serializers import BudgetSerializer


class MyBudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing budgets of an authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name",)

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(author=user)


class MySharedBudgetViewSet(MyBudgetViewSet):
    """
    ViewSet for viewing and editing shared budgets of an authenticated user.
    """

    def get_queryset(self):
        return self.request.user.shared_budgets.all()
