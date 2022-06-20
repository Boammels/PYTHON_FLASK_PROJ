''' Test message sendlater '''
import datetime
from datetime import timezone
import pytest
from message import message_sendlater
from channel import channels_create, channel_join
from auth import auth_register
from Error import AccessError

# These tests will make the messages send slightly into the future, so they are
# able to be visually cheked if they do in fact send later. It is difficult
# to properly test this function without using visual tests.

def test_message_sendlater_average():
    ''' Test message sendlater average '''
    ownerDict = auth_register("bossman321fsd@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", True)
    userDict = auth_register("testdhgdfs@gmail.com", "123456", "happy", "trump")
    channel_join(userDict['token'], channelResponse['channel_id'])
    # This user can choose to send a message to this channel at some time in the
    # future
    msgSendLater = message_sendlater(userDict['token'], channelResponse['channel_id'], "You shouldsee this in the future", (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp())
    assert 'message_id' in msgSendLater

def test_message_sendlater_large_string():
    ''' Test message sendlater large strings'''
    userDict = auth_register("testruy34@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(userDict['token'], "My Channel", False)
    # Over 1000 characters should produce a value error
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(userDict['token'], channelResponse['channel_id'], "L" * 1001, (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp())
    # Long messages under 1000 characters should be fine
    assert message_sendlater(userDict['token'], channelResponse['channel_id'], "L" * 999, (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp()) != {}

def test_message_sendlater_wrong_channel():
    ''' Test message sendlater wrong channel '''
    ownerDict = auth_register("bossmangf@gmail.com", "123456", "Boss", "man")
    channelResponse = channels_create(ownerDict['token'], "My Channel", False)
    userDict = auth_register("testtest@gmail.com", "123456", "happy", "trump")
    # Cant send messages to channels that user is not in
    with pytest.raises(AccessError, match=r"*"):
        message_sendlater(userDict['token'], channelResponse['channel_id'], "You should see this in the future", (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp())
    #Cant send messages to channels that do not exist
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(ownerDict['token'], channelResponse['channel_id'] + 1, "You should see this in the future", (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp())

def test_message_sendlater_timetravel():
    ''' Test message sendlater - cant send messages in the past '''
    ownerDict = auth_register("teste@gmail.com", "123456", "happy", "trump")
    channelResponse = channels_create(ownerDict['token'], "My Channel", False)
    # Cant ask for messages to be sent in the past
    with pytest.raises(ValueError, match=r"*"):
        assert message_sendlater(ownerDict['token'], channelResponse['channel_id'], "You should see this in the future", (datetime.datetime.utcnow()+datetime.timedelta(seconds=-60)).replace(tzinfo=timezone.utc).timestamp())
