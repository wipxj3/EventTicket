from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ticket.models import RegisterForm
from django.template import RequestContext, Context
from django import forms
from django.forms.widgets import *

@login_required
def ticket_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('ticket/index.html')

def register_view(request):
    success = ''
    error = ''
    
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm_password', '')

    if request.method == 'POST':
        if email != '' and password != '' and confirm_password != '':
            if email.find('@') == -1:
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