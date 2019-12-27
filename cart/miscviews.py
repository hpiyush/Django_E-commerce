# # import razorpay.resources.payment as payment
# import razorpay
import random
import string
# from django.shortcuts import (
#     render, redirect,
#     reverse, get_object_or_404
# )
# from django.contrib import messages
# from razorpay.errors import BadRequestError

from .models import CartItem, Order
# from products.models import Product
# from products.views import products_view
# from register.models import Profile
from datetime import date
import datetime
# from django.contrib.auth.decorators import login_required


def get_user_pending_order(request):
    order = Order.objects.get_or_create(owner=request.user, is_ordered=False, is_cart=True)
    print(order)
    # if order.exists():
    cart = CartItem.objects.filter(cart=order[0])
    print(f'{cart}, cartcart')
    # print(cart[0])
    # cart = all_carts.filter(is_ordered=False)
    print(f'{cart} == cart[0]')
    if cart.exists():
        return cart
    return 0

# def get_user_order(request):
#     order = Order.objects.filter(owner=request.user, is_ordered=True)
#     if order.exists():
#         return order
#     return0


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


