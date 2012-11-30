from django.db import models

from django import forms
from django.forms.widgets import *

# A simple contact form with four fields.
class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()
