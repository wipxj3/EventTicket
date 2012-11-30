from lettuce import *
import socket


@step(u'Given the ip address of server')
def given_the_ip_address_of_server(step):
    world.ip = "0.0.0.0"
    
@step(u'And the port number')
def and_the_port_number(step):
    world.port = 8080
    
@step(u'When I connect to server')
def when_i_connect_to_server(step):
    world.status = connect_to_server(world.ip, world.port)
    
@step(u'Then I get "([^"]*)"')
def then_i_get(step, expected):
    assert world.status == expected
    
@step(u'Given the ip address of the localhost')
def given_the_ip_address_of_server(step):
    world.ip = "127.0.0.1"
    
@step(u'And the port number')
def and_the_port_number(step):
    world.port = 80
    
@step(u'When I connect to server')
def when_i_connect_to_server(step):
    world.status = connect_to_server(world.ip, world.port)
    
@step(u'Then I get "([^"]*)"')
def then_i_get(step, expected):
    assert world.status == expected

def connect_to_server(ip,port):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.settimeout(5)
    status = "not connected"
    if clientSocket.connect_ex((world.ip, world.port)) == 0:
        status = "Connection established"
    return status
