__author__ = 'eduard'

from django import forms
from bootstrap3 import forms as bforms

class AuthForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")