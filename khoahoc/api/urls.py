from django.urls import path
from . import views

urlpatterns = [
    path('listkhoahoc', views.KhoahocApiView.as_view(), name='khoahoc'),
]