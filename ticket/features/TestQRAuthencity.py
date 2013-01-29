from lettuce import *

@step(u'Given a QR.PNG file with the encoded code')
def given_a_file_with_the_encoded_code(step):
    world.file = open('qr.png', 'rb')
    
@step(u'When I decode the QR code from PNG')
def when_i_decode_the_qr_code_from_png(step):
    world.hash = decode(world.file)
    
@step(u'And lookup the hash in the database')
def and_lookup_the_hash_in_the_database(step):
    world.user_hashes = fetch_hash_db()
    
@step(u'Then I get "([^"]*)"')
def then_i_get(step, expected):
    status = validate_ticket(world.user_hashes, world.hash)
    assert status == expected

def decode(fname):
    return 1
    
def fectch_hash():
    return 0
    
def validate_ticket(array, elem):
    for item in enumerate(array):
        if item == elem:
            return "Valid Ticket"
        return "Invalid Ticket"
