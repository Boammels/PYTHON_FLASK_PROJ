''' test message unpin '''
import pytest
from message import message_send, message_pin, message_unpin
from channel import channels_create, channel_join
from auth import auth_register

def test_message_unpinned_message():
    ''' test message unpin - message doesnt exist'''
    #Try to unpin a message that does not exist
    ownerDict = auth_register("bossmanhgf4@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", False)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(ownerDict['token'], msg['message_id'])
    
def test_message_unpin_average_case():
    ''' test message unpin - average case '''
    ownerDict = auth_register("bossmankgjhh@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", False)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    # Assume this message has a message id of 1
    # Owner pins own message
    message_pin(ownerDict['token'], msg['message_id'])
    # Owner unpins this message
    assert message_unpin(ownerDict['token'], msg['message_id']) == {}

def test_unpin_message_not_owner():
    ''' test message unpin - not authorised to unpin'''
    ownerDict = auth_register("bossmansfgd@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")
    # Assume this message has a message id of 1
    # Owner pins own message
    message_pin(ownerDict['token'], msg['message_id'])
    
    userDict = auth_register("testbxvb9i@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    #Assume this nessage has message_id 2
    # Normal user cant pin messages
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(userDict['token'], msg['message_id'])

def test_not_channel_member():
    ''' test message unpin  - not channel memeber - unauthorised'''
    ownerDict = auth_register("bossmanadsfa4323@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Pin the owner message")

    message_pin(ownerDict['token'], msg['message_id'])
    otherChnOwner = auth_register("newkhjgfkhj@gmail.com", "123456", "Other", "channel") 
    channelResponse2 = channels_create(otherChnOwner['token'], "My Channel", True)
    #Attempt to unpin the 1st message that is currently pinned to the first channel from within the second channel, shouldn't work
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(otherChnOwner['token'], msg['message_id'])
