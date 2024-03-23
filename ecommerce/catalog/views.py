import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Basket, BasketItem, Review 

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
    if not created:
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
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
        for item in basket.basketitem_set.all():
            print(item.product.title)  # Print the title of the product
        return render(request, 'catalog/checkout.html', {'basket': basket})
    else:
        return redirect('login')

# Remove items from checkout basket 
def remove_from_basket(request, item_id):
    if request.method == 'POST':
        item = BasketItem.objects.get(id=item_id)
        item.delete()
    return redirect('checkout')

# Payment page view
def payment(request):
    return render(request, 'catalog/payment.html')

# Stripe payment view
@csrf_exempt
def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        token = request.POST['stripeToken']

        charge =  stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Example charge',
            source=token,
        )

        return render(request, 'catalog/charge.html')

# Reviews page view

def reviews(request):
    reviews = Review.objects.all()  # Get all reviews
    return render(request, 'catalog/reviews.html', {'reviews': reviews})

def create_review(request):
    if request.method == 'POST':
        review = Review()
        review.user = request.user
        review.product = Product.objects.get(pk=request.POST['product_id'])
        review.rating = request.POST['rating']
        review.comment = request.POST['comment']
        review.save()
    return redirect('reviews')