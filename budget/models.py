from django.db import models
from django.contrib.auth.models import User

from budget.enums import ExpenseCategory


class Budget(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    shared_account = models.ManyToManyField(User, related_name="shared_budgets")
    income = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Expense(models.Model):
    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    category = models.CharField(max_length=20, choices=ExpenseCategory.choices)
