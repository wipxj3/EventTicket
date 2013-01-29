from django.db import models

from django import forms
from django.forms.widgets import *

# A simple contact form with four fields.
class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

class EmailNotification(models.Model):
    email_notification_name = models.CharField(max_length=80)
    email_notification_content = models.TextField()

class EmailNotificationForm(forms.Form):
    email_notification_name = forms.CharField(required=True)
    email_notification_content = forms.CharField(widget=forms.widgets.Textarea())

class EmailNotificationExecutionForm(forms.Form):
    notification_choices = EmailNotification.objects.all()
    field_choices = []
    for choice in notification_choices:
        field_choices.append((choice.email_notification_name, choice.email_notification_name))

    email_notification_name = forms.ChoiceField(required=True, choices=field_choices)