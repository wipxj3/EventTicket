from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ticket.models import RegisterForm, EmailNotificationForm, EmailNotification
from django.template import RequestContext, Context
from django import forms
from django.forms.widgets import *
import re

@login_required
def ticket_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('ticket/index.html')

def bad_register_view(request):
    success = ''
    error = ''
    
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm_password', '')

    if request.method == 'POST':
        #Decompose conditional
        if email != '' and password != '' and confirm_password != '':
            #Introduce explaining variable
            if not re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                error += 'Email isn\'t valid. '
            if password != confirm_password:
                error += 'Passwords don\'t match. '
            #Consolidate conditional fragments
            return render_to_response('ticket/register.html', {'form': RegisterForm(),
                'success': success,
                'error': error,                                              
                },
                RequestContext(request))
        else:
            error = 'You must complete all fields. '
            #Consolidate conditional fragments
            return render_to_response('ticket/register.html', {'form': RegisterForm(),
                'success': success,
                'error': error,                                              
                },
                RequestContext(request))
            

    if error == '':
        success = 'You have registered successfully .'

    #Inline temp
    response = render_to_response('ticket/register.html', {'form': RegisterForm(),
        'success': success,
        'error': error,                                              
        },
        RequestContext(request))
    return response

def register_view(request):
    success = ''
    error = ''
    
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm_password', '')

    all_required_fields_are_set = email != '' and password != '' and confirm_password != ''
    email_is_valid = re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)

    if request.method == 'POST':
        if all_required_fields_are_set:
            if not email_is_valid:
                error += 'Email isn\'t valid. '
            if password != confirm_password:
                error += 'Passwords don\'t match. '
        else:
            error = 'You must complete all fields. '  

    if error == '':
        success = 'You have registered successfully .'

    return render_to_response('ticket/register.html', {'form': RegisterForm(),
        'success': success,
        'error': error,                                              
        },
        RequestContext(request))

def email_notification_add(request):
    messages = []
    if request.method == 'POST':
        form = EmailNotificationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['email_notification_name']
            content = form.cleaned_data['email_notification_content']
            notification = EmailNotification(email_notification_name = name, email_notification_content = content)
            notification.save()
            # Set success message here, and display the same form
            messages.append("Email notification added successfully")
    else:
        form = EmailNotificationForm()
    return render(request, 'emails/email_notification_add.html', {'form': form, 'messages' : messages})

def email_notification_list(request):
    notifications = EmailNotification.objects.all()
    return render(request, 'emails/email_notification_list.html', {'notifications': notifications})