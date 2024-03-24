from django.contrib import admin
from .models import Category, Product, Basket, BasketItem, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.site_header = 'Cosmic Commerce Admin Portal'
admin.site.site_title = 'Admin Operations'