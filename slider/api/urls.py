from django.urls import path
from . import views

urlpatterns = [
    path('', views.SliderApiView.as_view(), name='slider'),
]