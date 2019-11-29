from django.shortcuts import render

# Create your views here.
def test_hook(request):
    return render(request, 'hooks/test_hook.html')