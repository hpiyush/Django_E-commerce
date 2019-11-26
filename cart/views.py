import razorpay
import random
import string
from django.shortcuts import (
    render, redirect,
    reverse, get_object_or_404
)
from django.contrib import messages
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
    print(order_item)
    order_item.quantity += 1
    order_item.save()
    user_order, status = Order.objects.get_or_create(owner=user_profile.user, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request, "Item added to cart")
    return redirect(reverse(products_view))


# Create your views here.
@login_required
def cart_view(request):
    client = razorpay.Client(auth=("rzp_test_FyUhgWReVhAYTk", "5fu4IEYGM13tzrj82gG3zO30"))
    client.set_app_details({"title": "DjangoProject", "version": "0.1"})

    existing_order = get_user_pending_order(request)
    order = existing_order[0].items.all()
    total_per = [i.product.price * i.quantity for i in order]
    total = sum(total_per)

    DATA = {
        'amount': float(total * 100),
        'currency': 'INR',
        'receipt': generate_order_id(),
        'payment_capture': 1,
    }
    returned = client.order.create(data=DATA)

    context = {
        'order': order,
        'order_id': returned['id'],
        'total': total,
        'razor_price': total * 100,
    }
    return render(request, 'cart.html', context)


def get_user_pending_order(request):
    order = Order.objects.filter(owner=request.user, is_ordered=False)
    if order.exists():
        return order
    return 0


@login_required
def remove_from_cart(request, id):
    print(request, id)
    product = Product.objects.filter(id=id).first()
    order_item = CartItem.objects.filter(product=product).first()
    order_item.quantity -= 1
    order_item.save()
    if order_item.quantity < 1:
        CartItem.objects.filter(product=product).delete()

    return redirect(reverse(cart_view))


@login_required
def buy_now(request, id):
    item = Product.objects.filter(id=id).first()
    client = razorpay.Client(auth=("rzp_test_FyUhgWReVhAYTk", "5fu4IEYGM13tzrj82gG3zO30"))
    client.set_app_details({"title": "DjangoProject", "version": "0.1"})
    DATA = {
        'amount': float(item.price * 100),
        'currency': 'INR',
        'receipt': generate_order_id(),
        'payment_capture': 1,
    }
    returned = client.order.create(data=DATA)
    # print(client.order.fetch('items'))

    context = {
        'item': item,
        'order_id': returned['id'],
        'razor_price': item.price * 100
    }
    return render(request, 'products/buy_now.html', context)
