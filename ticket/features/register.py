from lettuce import before, step, world
from lettuce.django import django_url
from lxml import html
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the register url')
def access_url(step):
    url = django_url('register/')
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    
@step(r'I enter a valid email')
def enter_valid_email(step):
    world.email = 'a@a.com'
    
@step(r'I enter an invalid email')
def enter_invalid_email(step):
    world.email = 'a@'
    
@step(r'I enter a valid password')
def set_password(step):
    world.password = 'qwerty'
    
@step(r'I manage to confirm the password')
def passwords_match(step):
    world.confirm_password = world.password
    
@step(r'I submit the form')
def submit_form(step):
    url = django_url('register/')
    response = world.browser.post(url, {'username': world.email, 'password': world.password, 
                                        'confirm_password': world.confirm_password})
    world.dom = html.fromstring(response.content)
    
@step(r'I get register success message')
def get_success_message(step):
    register_success = world.dom.cssselect('#register_success')
    assert len(register_success) == 1
    
@step(r'I get register error message')
def get_error_message(step, message):
    register_error = world.dom.cssselect('#register_error')
    assert len(register_error) == 1
