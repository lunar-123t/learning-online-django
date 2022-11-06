from django.urls import path
from . import views
urlpatterns = [
    path('listmess', views.chatApiView.as_view(), name='mess'),
    path('submit', views.chatCreate.as_view(), name='mess'),

]