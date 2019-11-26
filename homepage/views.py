from django.shortcuts import render
# from cart.models import Cart


# Create your views here.
def home_view(request):
    context = {
        'page': {
            'page_title': 'Home',
            'nav_head': 'Powered by Django',
        },
    }
    return render(request, 'home.html', context)
