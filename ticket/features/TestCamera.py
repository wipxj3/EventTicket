from lettuce import *


@step(u'Given camera device is connected')
def given_camera_device_is_connected(step):
    world.handle = get_device_handle()
    assert world.handle > 0, 'Camera not connected!'
    
@step(u'When the snapshot is taken')
def when_the_snapshot_is_taken(step):
    world.snap = take_snapshot(world.handle)
    
@step(u'And the error correction is performed')
def and_the_error_correction_is_performed(step):
    world.correction = error_correction(world.snap)
    
@step(u'Then I get "([^"]*)"')
def then_i_get(step, expected):
    status = validate_snap(world.correction)
    assert status == expected
    
def get_device_handle():
    return -1
    
def take_snapshot(handle):
    return -1
    
def error_correction(snap):
    return -1

def validate_snap(correction):
    if correction > 0:
        return "Sample approved"
    return "Sample rejected. Try Again..."
