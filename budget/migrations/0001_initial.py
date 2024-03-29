# Generated by Django 3.2.15 on 2022-09-08 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('income', models.DecimalField(decimal_places=10, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets',
                                             to=settings.AUTH_USER_MODEL)),
                ('shared_account',
                 models.ManyToManyField(null=True, related_name='shared_budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('category', models.CharField(
                    choices=[('EDUCATION', 'Education'), ('HOME', 'Home'), ('TRAVEL', 'Travel'),
                             ('CLOTHING', 'Clothing'), ('FOOD', 'Food'), ('SAVINGS', 'Savings'),
                             ('ENTERTAINMENT', 'Entertainment')], max_length=20)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses',
                                             to='budget.budget')),
            ],
        ),
    ]
