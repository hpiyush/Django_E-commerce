from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Catagory
from posts.models import Post


# Create your views here.
def home_view(request):
    context = {
        'page': {
            'page_title': 'Home',
            'nav_head': 'Powered by Django',
        },
    }
    return render(request, 'home.html', context)


def search_function(request):
    global query, products_queryset, posts_queryset
    if request.method == 'POST':
        query = request.POST['search']
        products_queryset = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        posts_queryset = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        print(products_queryset)
        print(request.POST['search'])

    context = {
        'query': query,
        'products_queryset': products_queryset,
        'posts_queryset': posts_queryset,
    }
    return render(request, 'products/search.html', context)


def filter_block_one_books(request, filter):
    catagory = Catagory.objects.get(name=filter)
    products = Product.objects.filter(catagory=catagory)

    context = {
        'filter': filter,
        'products': products,
    }
    return render(request, 'products/products_filter.html', context)
