''' Test message unrect '''
import pytest
from message import message_send, message_react, message_unreact
from channel import channels_create, channel_join
from auth import auth_register

def test_message_unreact_average():
    ''' Test message unrect average case '''
    ownerDict = auth_register("bossmanfds3276@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    # Assume this message has message_id 1
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "Unreact to this message")
    userDict = auth_register("test4235345hfghvbc@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    message_react(userDict['token'], msg['message_id'], 1)
    # Check we can successfully unreact to a message we have reacted to
    assert message_unreact(userDict['token'], msg['message_id'], 1) == {}
    # Already unreacted, cannot do it again
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(userDict['token'], msg['message_id'], 1)

def test_message_unreact_unauthorised():
    ''' Test message unrect unathorised to unreact'''
    ownerDict = auth_register("bossman64523bfg@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    # Assume this message has message_id 1
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "React to this message")
    userDict = auth_register("test96543@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    message_react(userDict['token'], msg['message_id'], 2)
    userDict2 = auth_register("test2hfg36@gmail.com", "123456", "test", "user")
    channel_join(userDict2['token'], channelResponse['channel_id'])
    # Should not be able to unreact another users message
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(userDict2['token'], msg['message_id'], 1)
