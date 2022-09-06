from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.CreateUserView.as_view()),
]