from django import forms
from .models import CartItem

class Cart(forms.Form):
    class meta:
        model = CartItem
        fields = ['quantity']
        widgets = {'forms.IntegerField()': forms.IntegerField(),}
