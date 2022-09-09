from rest_framework import serializers
from budget.models import Budget, Expense
from codes import Code


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
            "shared_accounts",
            "income",
            "created_at",
            "expenses",
        ]

    def validate_shared_accounts(self, shared_accounts):
        if self.context['request'].user in shared_accounts:
            raise serializers.ValidationError({"code": Code.SELF_SHARE.name, "details": Code.SELF_SHARE.value})
        return shared_accounts

    def create(self, validated_data):
        expenses = validated_data.pop("expenses", None)
        shared_accounts = validated_data.pop("shared_accounts", None)

        budget = Budget.objects.create(**validated_data)

        if shared_accounts:
            for s_a in shared_accounts:
                budget.shared_accounts.add(s_a)

        if expenses:
            for expense in expenses:
                Expense.objects.create(budget=budget, **expense)

        return budget
