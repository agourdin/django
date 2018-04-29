from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email","username","password1","password2")


class UserProfileBasic(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]


class UserProfileStaff(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]

class UserProfileStudent(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]

class UserProfileWeb(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]
