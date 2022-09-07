from rest_framework import serializers
from budget.models import Budget, Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'budget', 'amount']


class BudgetInputExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['amount', 'category']


class BudgetSerializer(serializers.ModelSerializer):
    expenses = BudgetInputExpenseSerializer(many=True)

    class Meta:
        model = Budget
        fields = ['id', 'name', 'author', 'shared_account', 'income', 'created_at', 'expenses']

    def create(self, validated_data):
        expenses_data = validated_data.pop("expenses")
        shared_account = validated_data.pop("shared_account")
        budget = Budget.objects.create(**validated_data)

        for s_a in shared_account:
            budget.shared_account.add(s_a)

        for expense_data in expenses_data:
            Expense.objects.create(budget=budget, **expense_data)

        return budget
