import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Product, Basket  

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

