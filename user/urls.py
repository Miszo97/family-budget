from django.urls import path
from user import views
from budget.views import BudgetViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'me/budgets', BudgetViewSet, basename='budget')
urlpatterns = router.urls

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
]

urlpatterns += router.urls
