''' Test message remove '''
import pytest
from message import message_send, message_remove
from channel import channels_create, channel_join
from auth import auth_register

def test_message_remove_average_case():
    ''' Test message remove average case '''
    ownerDict = auth_register("testp@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    #Assume send messages start at message_id 1
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "This is a test message")
    # Owner should be able to remove a message they sent
    assert message_remove(ownerDict['token'], msg['message_id']) == {}

def test_message_remove_double():
    ''' Test message remove message twice '''
    ownerDict = auth_register("test980890@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    msg = message_send(ownerDict['token'], channelResponse['channel_id'], "This is a test message")
    assert message_remove(ownerDict['token'], msg['message_id']) == {}
    #As the message has been removed, should not be able to remove it again
    with pytest.raises(ValueError, match=r"*"):
        message_remove(ownerDict['token'], msg['message_id'])

def test_message_remove_unauthorised():
    ''' Test message remove unauthorised '''
    ownerDict = auth_register("bossma56767n@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    message_send(ownerDict['token'], channelResponse['channel_id'], "React")
    userDict = auth_register("test56465@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    msg2 = message_send(userDict['token'], channelResponse['channel_id'], "My own message")
    # A normal user should be able to delete their own message
    assert message_remove(userDict['token'], msg2['message_id']) == {}
    #This user is not the original sender, or an owner or an admin, therefore
    #they should not be able to remove the message that has been sent (id 1)
    with pytest.raises(ValueError, match=r"*"):
        message_remove(userDict['token'], msg2['message_id'])
