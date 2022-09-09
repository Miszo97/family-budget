# Generated by Django 4.1.1 on 2022-09-09 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='shared_account',
        ),
        migrations.AddField(
            model_name='budget',
            name='shared_accounts',
            field=models.ManyToManyField(related_name='shared_budgets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='budget',
            name='income',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
