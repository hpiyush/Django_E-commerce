from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email here'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Retype Password'}),

        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'image']
