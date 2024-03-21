from django.db import models
from django.contrib.auth.models import User

# Category model, allowing for the creation of categories for products
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Product model, allowing for the creation of products with a description, price, and category
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=200, default='Default Title')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description

# Basket model
class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='BasketItem')

    def total_cost(self):
        return sum(item.total_price() for item in self.basketitem_set.all())
    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.basketitem_set.all())

# Basket model, allowing for the creation of a basket for a user
class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity
