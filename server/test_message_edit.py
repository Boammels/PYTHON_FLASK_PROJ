''' test mesage edit '''
import pytest
from Error import AccessError
from message import message_send, message_edit
from channel import channels_create, channel_invite
from auth import auth_register

def test_message_edit_message_message_id_match():
    ''' test mesage edit '''
    userDict = auth_register("test@gmail.com", "123456bxvc", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    msg = message_send(userDict['token'], channelResponse['channel_id'], "This is a test message")
    # Assume this message was given a message_id of 1
    # Assert that if someone has the correct token that matches the message_id,
    #it should work (return nothing)

    assert message_edit(userDict['token'], msg['message_id'], "New message") == {}
    # A user that has not sent this message shouldn't be able to edit it
    newUserDict = auth_register("new@gmail.com", "123456", "New", "User")
    with pytest.raises(AccessError, match=r"*"):
        message_edit(newUserDict['token'], msg['message_id'], "New message")

def test_message_edit_correct_user():
    ''' test mesage edit '''
    #Assume this user is an admin
    ownerDict = auth_register("bossman@gmail.com", "123456xbc", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "lol", 1)
    cId = channelResponse['channel_id']
    userDict = auth_register("test1@gmail.com", "b123456xbvc", "happy", "trump")
    channel_invite(cId, ownerDict['token'], userDict['u_id'])
    msg = message_send(userDict['token'], cId, "This is a test message")
    # Assume this message was given a message_id of 0
    # Owner should be able to edit any message
    assert message_edit(ownerDict['token'], msg['message_id'], "Overide message") == {}
    #Assume this user is an owner of the channel
