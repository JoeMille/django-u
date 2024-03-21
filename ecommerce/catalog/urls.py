from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'), 
    path('register/', views.register, name='register'), 
    path('products/', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('charge/', views.charge, name='charge'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
]