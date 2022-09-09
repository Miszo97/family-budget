from django.urls import path
from rest_framework.routers import DefaultRouter

from budget.views import BudgetViewSet
from user import views

router = DefaultRouter()
router.register(r"me/budgets", BudgetViewSet, basename="budgets")
router.register(r"me/shared-budgets", BudgetViewSet, basename="shared-budgets")

urlpatterns = router.urls

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
]

urlpatterns += router.urls
