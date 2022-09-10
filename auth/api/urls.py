from django.urls import path

from auth.api.views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='auth_register'),

]