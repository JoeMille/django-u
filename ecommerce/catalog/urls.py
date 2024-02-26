from django.urls import path, include 
from . import views

urlpatterns = [
    path('', include('catalog.urls')),
    path('', views.base_view, name='base'),
]