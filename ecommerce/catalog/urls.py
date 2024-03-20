from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'), 
    path('register/', views.register, name='register'), 
    path('products/', views.products, name='products'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    
]