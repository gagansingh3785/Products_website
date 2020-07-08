from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    "aria-label": "Username",
                    "aria-describedby": "basic-addon1",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
        }


class UserInformation(ModelForm):
    class Meta:
        model = Info
        fields = ['type_of_user', 'phone']
        widgets = {
            'type_of_user': forms.Select(
                choices=Info.category,
                attrs={
                    'id': 'choice-field',
                    'class': 'form-control',

                }

            ),
            'phone': forms.TextInput(
                attrs={
                    'type': 'tel',
                    'class': 'form-control',
                    'placeholder': 'Phone Number',

                }
            ),
        }




class UpdateInfo(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs=
                                                                  {
                                                                      'type': 'email',
                                                                      'class': 'form-control',
                                                                  }))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs=
                                                                     {
                                                                         'class': 'form-control',
                                                                     }))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs=
                                                                  {
                                                                      'type': 'tel',
                                                                      'class': 'form-control'
                                                                   }))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs=
                                                                     {
                                                                         'class': 'form-control'
                                                                     }))
