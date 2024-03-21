import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Product, Basket, BasketItem  

# Index page view
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = AuthenticationForm()

    # Fetch the basket for the current user
    basket = None
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
    
    # Fetch featured products 
    featured_products = Product.objects.filter(featured=True)[:3]

    return render(request, 'catalog/index.html', {'form': form, 'basket': basket})

# Add products to user basket
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket_item, created = BasketItem.objects.get_or_create(product=product, basket=basket)
    basket_item.quantity += 1
    basket_item.save()
    return redirect('products')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/register.html', {'form': form})

# Products page view
def products(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})

# Checkout page view
def checkout(request):
    return render(request, 'catalog/checkout.html')