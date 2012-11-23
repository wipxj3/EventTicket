from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()
    
@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    
@step(r'I am logged in')
def am_logged_in(step):
    assert True
    
@step(r'I am not logged in')
def am_not_logged_in(step):
    assert True
    
@step(r'I am redirected to "(.*)"')
def redirect(step, url):
    assert False
    
@step(r'I get the message "(.*)"')
def get_message(step, message):
    assert True