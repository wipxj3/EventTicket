from lettuce import before, step, world
from lettuce.django import django_url
from lxml import html
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the login url')
def access_login_url(step):
    url = django_url('login/')
    print 'URL = ', url
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see an input for username')
def see_form(step):
    text_input = world.dom.cssselect('#id_username')
    assert len(text_input) == 1
    
@step(r'I dont fill the password input')
def empty_password_input(step):
    pass
    
@step(r'I submit the form')
def submit_form(step):
    url = django_url('login/')
    response = world.browser.post(url, {'username': 'abc', 'password': ''})
    world.dom = html.fromstring(response.content)
    
@step(r'I get password empty error message')
def get_password_empty_error_message(step):
    error_container = world.dom.cssselect('#id_password_error')
    assert len(error_container) == 1