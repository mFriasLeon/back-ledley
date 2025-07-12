from django.urls import path
from .views.login_view import LoginView

urlpatterns = [
    path("token/", LoginView.as_view(), name="token_obtain"),
]
