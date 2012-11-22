__author__ = 'DEXTER'
# -*- coding: utf-8 -*-
from lettuce import *
from lxml import html
from django.test.client import Client
import nose.tools

@before.all
def set_browser():
    world.browser = Client()

@step(r'I am logged in "(.*)"')
def given_i_am_logged_in(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    #assert False, 'This step must be implemented'

@step(r'I see button "(.*)"')
def then_i_see_button(step, text):
    button = world.dom.cssselect('button')[0]
    assert button.text == text

@step(u'When I press add event')
def when_i_press_add_event(step):
    assert False, 'This step must be implemented'

@step(u'Then I see new event form')
def then_i_see_new_event_form(step):
    assert False, 'This step must be implemented'
