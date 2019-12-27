from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('Order', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=99.99, max_digits=1000, decimal_places=2)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.cart.owner} -> {self.product}'

class Order(models.Model):
    ref_code = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    is_cart = models.BooleanField(default=True)
    # items = models.ManyToManyField(CartItem)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.ref_code}'

    # def get_cart_items(self):
    #     return self.items.all()

    # def get_cart_total(self):
    #     return sum([item.product.price for item in self.items.all()])





#''''
# Session for current user
# cart for current user
# successful orders for current user -- must have mutiple orders
# ''''