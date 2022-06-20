''' test channel messages '''
import pytest
from Error import AccessError
from auth import auth_register
from message import message_send
from channel import channels_create, channel_messages, channel_join
def test_channel_messages1():
    ''' test channel messages '''
    #set up user
    authRegisterDict = auth_register("z3456782vc@ad.unsw.edu.au", "123456", "bob", "Hayden")
    token = authRegisterDict['token']
    #set up user2
    authRegisterDict2 = auth_register("z5356782bv@ad.unsw.edu.au", "129456", "Tom", "Hiddleson")
    token2 = authRegisterDict2['token']

    #user 1 set up channel
    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']
    channel_join(token2, channelId)

    #send message from user2 to user1's channel
    message_send(token, channelId, "do you like python")
    message_send(token2, channelId, "uccu")
    #out of total number
    with pytest.raises(ValueError):
        channel_messages(token, channelId, 3)

def test_channel_messages2():
    ''' test channel messages '''
    #invalid channel_id
    authRegisterDict = auth_register("z3456782vcd@ad.unsw.edu.au", "123456", "bob", "Hayden")
    token = authRegisterDict['token']
    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']
    with pytest.raises(ValueError):
        channel_messages(token, 452, 0)

def test_channel_messages3():
    ''' test channel messages '''
    authRegisterDict = auth_register("z3456782vdcd@ad.unsw.edu.au", "123456",
                                     "bob", "Hayden")
    token = authRegisterDict['token']
    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']
    reVal = channel_messages(token, channelId, 0)
    assert type(reVal) == dict

def test_channel_messages4():
    ''' test channel messages '''
    #user2 is not a memebr of channel1
    authRegisterDict = auth_register("z3456782cxvxcvc@ad.unsw.edu.au", "123456",
                                     "bob", "Hayden")
    token1 = authRegisterDict['token']
    #set up user2
    authRegisterDict2 = auth_register("z5356782xcvxabv@ad.unsw.edu.au", "129456",
                                      "Tom", "Hiddleson")
    token2 = authRegisterDict2['token']
    channelsCreateDict = channels_create(token1, 'Channel1', False)
    channelId = channelsCreateDict['channel_id']
    reVal = channel_messages(token1, channelId, 0)
    assert type(reVal) == dict
    with pytest.raises(AccessError):
        channel_messages(token2, channelId, 0)
