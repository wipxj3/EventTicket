from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

def mail_is_valid():
    return True

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    
@step(r'email is "(.*)"')
def set_email(step, email):
    world.email = email
    
@step(r'password is "(.*)"')
def set_password(step, value):
    world.password = ''
    
@step(r'confirm password is "(.*)"')
def passwords_match(step, value):
    world.confirm_password = ''
    assert False
    
@step(r'I am redirected to "(.*)"')
def redirect(step, url):
    assert False
    
@step(r'I get error message "(.*)"')
def get_message(step, message):
    assert True
