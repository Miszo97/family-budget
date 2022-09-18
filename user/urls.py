from django.urls import path
from rest_framework.routers import DefaultRouter

from budget.views import MyBudgetViewSet, MySharedBudgetViewSet
from user import views

router = DefaultRouter()
router.register(r"me/budgets", MyBudgetViewSet, basename="my-budgets")
router.register(r"me/shared-budgets", MySharedBudgetViewSet, basename="my-shared-budgets")

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
]

urlpatterns += router.urls
