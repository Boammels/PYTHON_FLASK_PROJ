''' Test message rect '''
import pytest
from message import message_send, message_react
from channel import channels_create, channel_join
from auth import auth_register

def test_message_react_average():
    ''' Test message rect avreage '''
    ownerDict = auth_register("bossman76@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    # Assume this message has message_id 1
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "React to this message")
    userDict = auth_register("test31@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    # Check that a user can react to another users message
    assert message_react(userDict['token'], msg['message_id'] , 1) == {}
    userDict2 = auth_register("test2365@gmail.com", "123456", "test", "user")
    channel_join(userDict2['token'], channelResponse['channel_id'])
    # Check that a different user can react to the same message, with a different react id
    assert message_react(userDict2['token'], msg['message_id'] , 1) == {}
    
def test_message_react_multiple():    
    ''' Test message rect mutliple '''
    ownerDict = auth_register("bossman2345213@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    # Assume this message has message_id 1
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "React to this message")
    userDict = auth_register("test8755@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    # Check that a user can react to another users message
    assert message_react(userDict['token'], msg['message_id'], 1) == {}
    userDict2 = auth_register("test2@gmail.com", "123456", "test", "user")
    channel_join(userDict2['token'], channelResponse['channel_id'])
    assert message_react(userDict2['token'], msg['message_id'], 1) == {}

def test_message_react_invalid_message_id():
    ''' Test message rect invalid message id '''
    ownerDict = auth_register("bossman2354v@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    # Assume this message has message_id 1
    message_send(ownerDict['token'], channelResponse['channel_id'], "React to this message")
    userDict = auth_register("test4523452@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    # A user should not be able to react to a message that does not exist
    with pytest.raises(ValueError, match=r"*"):
        message_react(userDict['token'], 12345678, 1)
