from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import *
from django_site_users.LoginForm import LoginForm

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/login/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render(request, 'login.html', {
        'form': form,
        })

def main_page(request):
    return render_to_response('index.html')

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')