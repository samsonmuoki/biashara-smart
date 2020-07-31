from django import forms
# from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from .models import Client


class ClientSignUpForm(UserCreationForm):
    """Client registration details."""

    # TODO validate username to only accept phone numbers
    username = forms.CharField(
        max_length=15, required=True, help_text="your phone number"
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        """Form details."""

        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
        )


class ClientLoginForm(forms.Form):
    """Client login details."""

    phone_number = forms.CharField(max_length=15)
    # username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
