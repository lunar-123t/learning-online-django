from django.urls import path

from auth.api.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
]