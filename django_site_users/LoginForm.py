from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput