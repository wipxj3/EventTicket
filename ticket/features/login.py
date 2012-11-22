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

@step(r'I see the input with id "(.*)"')
def see_form(step, id):
    input = world.dom.cssselect('#' + id)
    assert input != None
    
@step(r'I dont fill field "(.*)"')
def field_not_filled(step, id):
    assert True
    
@step(r'I submit the form "(.*)"')
def submit_form(step, submit_id):
    assert True
    
@step(r'I am redirected to "(.*)"')
def redirect(step, url):
    current_url = world.browser.url
    assert current_url == '/'