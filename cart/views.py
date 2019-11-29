import razorpay.resources.payment as payment
import razorpay
import random
import string
from django.shortcuts import (
    render, redirect,
    reverse, get_object_or_404
)
from django.contrib import messages
from django.views.generic import ListView
from razorpay.errors import BadRequestError

from .models import CartItem, Order
from products.models import Product
from products.views import products_view
from .forms import Cart
from register.models import Profile
from datetime import date
import datetime
from django.contrib.auth.decorators import login_required


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


@login_required
def add_to_cart(request, item_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=item_id).first()
    order_item, status = CartItem.objects.get_or_create(product=product)
    order_item.quantity += 1
    order_item.save()

    user_order, status = Order.objects.get_or_create(owner=user_profile.user, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.warning(request, 'Item added to cart')
    return redirect(reverse(products_view))


# Create your views here.
@login_required
def cart_view(request):
    existing_order = get_user_pending_order(request)
    order = existing_order[0].items.all()
    total_per = [i.product.price * i.quantity for i in order]
    total = sum(total_per)
    if total > 1:
        client = razorpay.Client(auth=("rzp_live_QY0VqVNR9qxYFo", "mO5s8vKpN6sP7tdTLpYmjypi"))
        client.set_app_details({"title": "DjangoProject", "version": "0.1"})
        DATA = {
            'amount': float(total * 100),
            'currency': 'INR',
            'receipt': generate_order_id(),
            'payment_capture': 1,
        }
        returned = client.order.create(data=DATA)
        print(returned)
        context = {
            'order': order,
            'order_id': returned['id'],
            'total': total,
            'razor_price': total * 100,
        }
        user_profile = get_object_or_404(Profile, user=request.user)
        Order.objects.get_or_create(owner=user_profile.user, is_ordered=True)
        return render(request, 'products/cart.html', context)
    else:
        messages.warning(request, 'No items in cart. Add items to view cart.')
        return redirect(reverse(products_view))

@login_required
def buy_now(request, id, *args, **kwargs):
    item = Product.objects.filter(id=id).first()
    client = razorpay.Client(auth=("rzp_live_QY0VqVNR9qxYFo", "mO5s8vKpN6sP7tdTLpYmjypi"))
    client.set_app_details({"title": "Django-Project", "version": "0.1"})
    DATA = {
        'amount': item.price * 100,
        'currency': 'INR',
        'receipt': generate_order_id(),
        'payment_capture': 1,
    }
    returned = client.order.create(data=DATA)

    context = {
        'item': item,
        'order_id': returned['id'],
        'razor_price': item.price * 100,
        'args': args,
        'kwargs':kwargs,
        'request': request,
    }

    return render(request, 'products/buy_now.html', context)


@login_required
def all_orders(request, *args, **kwargs):
    orders = Order.objects.filter(owner=request.user, is_ordered=False)
    all_items = [item.items.all() for item in orders]
    make_list = [[i, j] for i in orders for j in all_items[0]]

    context = {
        'make_list': make_list,
        'args': args,
        'kwargs': kwargs,
        'request': request,
    }
    return render(request, 'user/orders.html', context)



def get_user_pending_order(request):
    order = Order.objects.filter(owner=request.user, is_ordered=False)
    if order.exists():
        return order
    return 0

def get_user_order(request):
    order = Order.objects.filter(owner=request.user, is_ordered=True)
    if order.exists():
        return order
    return 0

@login_required
def remove_from_cart(request, id):
    product = Product.objects.filter(id=id).first()
    order_item = CartItem.objects.filter(product=product).first()
    order_item.quantity -= 1
    order_item.save()
    if order_item.quantity < 1:
        CartItem.objects.filter(product=product).delete()
    try:
        return redirect(reverse(cart_view))
    except BadRequestError:
        return redirect(reverse(products_view))
