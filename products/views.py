from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView


# Create your views here.
def products_view(request):
    context = {
        'products': Product.objects.all(),
        'page': {
            'page_title': 'Products',
            'nav_head': "Products",
            'nav1': "About",
            'nav2': "All Products",
            'navDrop': "Account",
            'navDrop1': "Orders",
            'navDrop2': "Cart",
            'navDrop3': "Settings",
            'navDrop4': "(LogOUt)",

        },
    }

    return render(request, 'products/products.html', context)

class ProductDetailView(DetailView):
    model = Product
    template = 'products/products.html'

# def order_view(request):
#