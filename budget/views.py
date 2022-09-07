from django.shortcuts import render
from budget.models import Budget, Expense
from budget.serializers import BudgetSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class BudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing budgets.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]