from django.urls import path
from . import views

urlpatterns = [
    path('listkhoahoc', views.KhoahocApiView.as_view(), name='khoahoc'),
    path('listlevel', views.Listlevel.as_view(), name='level'),
    path('listalllevel', views.ListAlllevel.as_view(), name='levelall'),
    path('search', views.SearchList.as_view(), name='levelall'),
    path('listvideo', views.BaihocApiView.as_view(), name='level'),
]