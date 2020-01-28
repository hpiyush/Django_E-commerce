import razorpay
from django.shortcuts import (
    render, redirect,
    reverse
)
from django.contrib import messages
from products.models import Product
from products.views import products_view
from django.contrib.auth.decorators import login_required
from .miscviews import *
from .models import CartItem, Order
from django.views.decorators.csrf import csrf_exempt



@login_required
def cart_view(request):
    existing_order = get_user_pending_order(request)
    print(f'{existing_order} = existing order')
    if existing_order == 0:
        messages.warning(request, 'No items in cart. Add items to view cart.')
        return redirect(reverse(products_view))
    else:

        # print(existing_order[0].cart)
        order = existing_order
        print(f'{order}, cartview')
        total_per = [i.product.price * i.quantity for i in order]
        total = sum(total_per)
        if total > 1:
            client = razorpay.Client(auth=("rzp_test_###########", "#############"))
            client.set_app_details({"title": "DjangoProject", "version": "0.1"})
            DATA = {
                'amount': float(total * 100),
                'currency': 'INR',
                'receipt': generate_order_id(),
                'payment_capture': 1,
            }
            returned = client.order.create(data=DATA)
            # print(returned['id'])
            context = {
                'order': order,
                'order_id': returned['id'],
                'total': total,
                'razor_price': total * 100,
            }
            order = Order.objects.get(owner=request.user, is_ordered=False, is_cart=True)
            order.ref_code = returned['id']
            order.save()
            print(order.ref_code)

            return render(request, 'products/cart.html', context)
        else:
            messages.warning(request, 'No items in cart. Add items to view cart.')
            return redirect(reverse(products_view))


@login_required
def add_to_cart(request, item_id):
    cart = Order.objects.get_or_create(owner=request.user, is_ordered=False, is_cart=True)
    product = Product.objects.filter(id=item_id).first()
    print(cart)
    order_item, status = CartItem.objects.get_or_create(cart=cart[0], product=product)
    order_item.quantity += 1
    order_item.save()
    # print(order_item.quantity)
    # print(order_item.product)
    messages.warning(request, 'Item added to cart')
    return redirect(reverse(products_view))


@login_required
def buy_now(request, id):
    product = Product.objects.filter(id=id).first()
    try:
        cart = Order.objects.get(owner=request.user, is_ordered=False, is_cart=False)
        cart.delete()
        cart.save()
    except:
        cart = Order.objects.create(owner=request.user, is_ordered=False, is_cart=False)
    order, status = CartItem.objects.get_or_create(cart=cart, product=product)
    order.quantity = 1
    order.save()
    if status:
        order.ref_code = generate_order_id()
        order.save()
    client = razorpay.Client(auth=("rzp_test_##############", "sefweWe#########M3"))
    client.set_app_details({"title": "Django-Project", "version": "0.1"})
    DATA = {
        'amount': product.price * 100,
        'currency': 'INR',
        'receipt': generate_order_id(),
        'payment_capture': 1,
    }
    returned = client.order.create(data=DATA)
    cart.ref_code = returned['id']
    cart.save()

    context = {
        'item': product,
        'order_id': returned['id'],
        'razor_price': product.price * 100,
    }
    return render(request, 'products/buy_now.html', context)

@csrf_exempt
@login_required
def order_success(request):
    if request.method == 'POST':
        payment_id = request.POST['razorpay_payment_id']
        order_id = request.POST['razorpay_order_id']
        signature = request.POST['razorpay_signature']
        client = razorpay.Client(auth=("rzp_test_############", "SJ####dncV8t###M3"))
        verify_details = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature,
        }
        verify = client.utility.verify_payment_signature(verify_details)
        if payment_id and order_id and signature and verify == None:
            user_order = Order.objects.get(owner=request.user, ref_code=order_id)
            user_order.is_ordered = True
            user_order.save()
            messages.warning(request, 'Payment Successful')
            return redirect(reverse(products_view))
        else:
            messages.warning(request, 'Payment Failed. Try Again')
            return redirect(reverse(products_view))
    else:
        messages.warning(request, 'An Error occured. Please try again.')
        return redirect(reverse(cart_view))
    # return render(request, 'user/order_event.html')


@login_required
def all_orders(request):
    orders = Order.objects.filter(owner=request.user, is_ordered=True)
    print(orders, "\n")
    make_list = []
    for item in orders:
        cart = CartItem.objects.filter(cart=item)
        for a in cart:
            print(f'{a} == {cart} == {item.ref_code} +> a, cart')
            make_list.append([item, a])
            print(make_list)

    context = {
        'make_list': make_list,
    }
    return render(request, 'user/orders.html', context)


@login_required
def remove_from_cart(request, id):
    try:
        order = Order.objects.get(owner=request.user, is_ordered=False, is_cart=True)
        product = Product.objects.filter(id=id).first()
        order_item = CartItem.objects.filter(cart=order, product=product).first()
        if order_item.quantity >= 1:
            order_item.quantity -= 1
            order_item.save()
            if order_item.quantity < 1:
                order_item.delete()
        return redirect(reverse(cart_view))
    except AttributeError:
        return redirect(reverse(cart_view))
