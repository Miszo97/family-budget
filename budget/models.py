from django.db import models
from django.contrib.auth.models import User

from budget.enums import ExpenseCategory


class Budget(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    shared_account = models.ManyToManyField(User, related_name="shared_budgets", null=True)
    income = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)


    def __repr__(self):
        return f"{name=}, {author=}, {income=}, shared_accounts={shared_account.all()}"


class Expense(models.Model):
    budget = models.ForeignKey(Budget, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    category = models.CharField(max_length=20, choices=ExpenseCategory.choices)

    def __str__(self):
        return f"Expense of budget {self.budget} with {amount=} and {category=}"
