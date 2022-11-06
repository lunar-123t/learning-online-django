from django.urls import path
from . import views
urlpatterns = [
    path('listmess', views.ChatApiView.as_view(), name='mess'),
    path('submit', views.ChatCreate.as_view(), name='mess'),

]