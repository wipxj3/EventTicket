from lettuce import before, step, world
from lettuce.django import django_url
from lxml import html
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()
    world.browser.session
    
@step(r'I access the logout url')
def access_url(step):
    url = django_url('logout/')
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    
@step(r'I am logged in')
def am_logged_in(step):
    url = django_url('/')
    response = world.browser.get(url)
    dom = html.fromstring(response.content)
    profile_username = dom.cssselect('#my_username')
    profile_username = []
    #assert len(profile_username) == 1
    
@step(r'I am not logged in')
def am_not_logged_in(step):
    url = django_url('/')
    response = world.browser.get(url)
    dom = html.fromstring(response.content)
    profile_username = dom.cssselect('#my_username')
    profile_username = []
    #assert len(profile_username) == 0
    
@step(r'I dont see my profile block on the page')
def not_see_profile_block_on_page(step):
    profile_username = world.dom.cssselect('#my_username')
    assert len(profile_username) == 0
    
@step(r'I get logout error message ')
def get_message(step):
    logout_error = world.dom.cssselect('#logout_error')
    assert len(logout_error) == 1