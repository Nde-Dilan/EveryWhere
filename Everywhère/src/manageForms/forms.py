from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import *

"""Differentes interfaces de login et register"""


class SingUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-input',
            'placeholder': 'john doe',
            'maxlength': "16",
            'minlength': "6"
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-input',
            'placeholder': 'end@gmail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'Choisissez un mot de passe',
            'maxlength': "22",
            'minlength': "8"
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-input',
            'placeholder': 'Retaper votre  mot de passe',
            'maxlength': "22",
            'minlength': "8"
        })

        # model = Proprietaire, Client

    # fields = '__all__'
    # username = forms.CharField(max_length=8)
    # tel = forms.IntegerField(widget=forms.NumberInput)
    # email = forms.EmailField()
    # password = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     "username": forms.TextInput(attrs={'class': "name", "placeholder": "Enter your username"}),
        #     "tel": forms.NumberInput(attrs={'class': "tel", "placeholder": "Enter your phone number"}),
        #     "Email": forms.TextInput(attrs={'class': "email", "placeholder": "Enter your email address"}),
        # }


class SingInForm(forms.Form):
    username = forms.CharField(max_length=8)
    password = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput)
