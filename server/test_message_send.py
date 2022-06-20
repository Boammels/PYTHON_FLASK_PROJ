''' Test message send '''
import pytest
from message import message_send
from channel import channels_create
from auth import auth_register
from Error import AccessError

def test_message_send_normal():
    ''' Test message send normal '''
    userDict = auth_register("testsd@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    assert message_send(userDict['token'], channelResponse['channel_id'], "This is a test message") != {}

def test_message_send_large_string():
    ''' Test message send large strings '''
    userDict = auth_register("testsgfd@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    # Over 1000 characters should produce a value error
    with pytest.raises(ValueError, match=r"*"):
        message_send(userDict['token'], channelResponse['channel_id'], "L" * 1005)
    # Long messages under 1000 characters should be fine
    assert message_send(userDict['token'], channelResponse['channel_id'], "L" * 999) != {}

def test_message_send_multiple_messages():
    ''' Test message send multiple messages '''
    userDict = auth_register("testadfsadfs@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    assert message_send(userDict['token'], channelResponse['channel_id'], "This is a test message") != {}
    assert message_send(userDict['token'], channelResponse['channel_id'], "Another one") != {}
    assert message_send(userDict['token'], channelResponse['channel_id'], "Another one") != {}
    assert message_send(userDict['token'], channelResponse['channel_id'], "Another one") != {}

def test_message_send_not_in_channel():
    ''' Test message send user not in channel '''
    userDict = auth_register("testadfsadfs322@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    userDict2 = auth_register("testsdf32@gmail.com", "123456", "happy", "trump")
    with pytest.raises(AccessError, match=r"*"):
        message_send(userDict2['token'], channelResponse['channel_id'], "No")
