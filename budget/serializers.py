from rest_framework import serializers
from budget.models import Budget, Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "budget", "amount"]


class BudgetInputExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["amount", "category"]


class BudgetSerializer(serializers.ModelSerializer):
    expenses = BudgetInputExpenseSerializer(many=True, required=False)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Budget
        fields = [
            "id",
            "name",
            "author",
            "shared_account",
            "income",
            "created_at",
            "expenses",
        ]

    def create(self, validated_data):
        expenses = validated_data.pop("expenses", None)
        shared_account = validated_data.pop("shared_account", None)

        budget = Budget.objects.create(**validated_data)
        
        if shared_account:
            for s_a in shared_account:
                    budget.shared_account.add(s_a)
        
        if expenses:
            for exepnse in expenses:
                Expense.objects.create(budget=budget, **exepnse)

        return budget
