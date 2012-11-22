from lettuce import *
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.settimeout(5)


@step(u'Given the ip address of server "([^"]*)"')
def given_the_ip_address_of_server(step, ip):
    world.ip = ip
    
@step(u'And the port number "([^"]*)"')
def and_the_port_number(step, port):
    world.port = int(port)
    
@step(u'When I connect to server')
def when_i_connect_to_server(step):
    world.status = connect_to_server(world.ip, world.port)
    
@step(u'Then I get "([^"]*)"')
def then_i_get_group1(step, expected):
    assert world.status == expected

def connect_to_server(ip,port):
    status = "not connected"
    if clientSocket.connect_ex((world.ip, world.port)) == 0:
        status = "Connection established"
    return status
