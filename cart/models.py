from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.product)

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
