from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email","username","password1","password2")
