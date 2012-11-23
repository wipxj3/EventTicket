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
    

@step(u'Given a "([^"]*)" file with the encoded code')
def given_a_group1_file_with_the_encoded_code(step, group1):
    assert False, 'This step must be implemented'
    
@step(u'When I decode the QR code from PNG')
def when_i_decode_the_qr_code_from_png(step):
    assert False, 'This step must be implemented'
    
@step(u'And lookup the hash in the database')
def and_lookup_the_hash_in_the_database(step):
    assert False, 'This step must be implemented'
    
@step(u'Then I get "([^"]*)"')
def then_i_get_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'Given camera device is connected "([^"]*)"')
def given_camera_device_is_connected_group1(step, group1):
    assert False, 'This step must be implemented'
    
@step(u'When the snapshot is taken')
def when_the_snapshot_is_taken(step):
    assert False, 'This step must be implemented'
    
@step(u'And the error correction is performed')
def and_the_error_correction_is_performed(step):
    assert False, 'This step must be implemented'


