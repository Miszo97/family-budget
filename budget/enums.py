from django.db import models
from django.utils.translation import gettext_lazy as _


class ExpenseCategory(models.TextChoices):
    EDUCATION = 'EDUCATION', _('Education')
    HOME = 'HOME', _('Home')
    TRAVEL = 'TRAVEL', _('Travel')
    CLOTHING = 'CLOTHING', _('Clothing')
    FOOD = 'FOOD', _('Food')
    SAVINGS = 'SAVINGS', _('Savings')
    ENTERTAINMENT = 'ENTERTAINMENT', _('Entertainment')
