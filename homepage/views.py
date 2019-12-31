from django.shortcuts import render
# from cart.models import Cart
from products.models import Product, Catagory


# Create your views here.
def home_view(request):
    context = {
        'page': {
            'page_title': 'Home',
            'nav_head': 'Powered by Django',
        },
    }
    return render(request, 'home.html', context)


def filter_block_one_books(request, filter):
    catagory = Catagory.objects.get(name=filter)
    products = Product.objects.filter(catagory=catagory)

    context = {
        'filter': filter,
        'products': products,
    }
    return render(request, 'products/products_filter.html', context)