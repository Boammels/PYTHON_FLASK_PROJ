''' test message pin '''
import pytest
from message import message_send, message_pin
from channel import channels_create, channel_join
from auth import auth_register

def test_message_pin_average_case():
    ''' test message pin normal case'''
    ownerDict = auth_register("bossman4321@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", False)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    # Assume this message has a message id of 1
    # Owner pins own message
    assert message_pin(ownerDict['token'], msg['message_id']) == {}

def test_message_pin_from_other_channel():
    ''' test message pin from other channel '''
    ownerDict = auth_register("bossman132@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    # message_id is assumed to be 1
    otherChnOwner = auth_register("new2@gmail.com", "123456", "Other", "channel")
    channels_create(otherChnOwner['token'], "My Channel", True)
    #Attempt to pin the 1st message from the second channel, shouldn't work
    with pytest.raises(ValueError, match=r"*"):
        message_pin(otherChnOwner['token'], msg['message_id'])

def test_pin_message_from_admin():
    ''' test message pin from admin'''
    ownerDict = auth_register("bossman73@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    # Owner pins own message
    assert message_pin(ownerDict['token'], msg['message_id']) == {}
    userDict = auth_register("test@gmail42.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    msg2 = message_send(userDict['token'], channelResponse['channel_id'], "New user message to pin")
    #Assume this nessage has message_id 2
    # Normal user cant pin messages
    with pytest.raises(ValueError, match=r"*"):
        message_pin(userDict['token'], msg2['message_id'])
    # Owner can pin though
    assert message_pin(ownerDict['token'], msg2['message_id']) == {}
    # Attempt to repin an already pinned message, shouldn't work
    with pytest.raises(ValueError, match=r"*"):
        message_pin(ownerDict['token'], msg2['message_id'])
