''' test channel join '''
import pytest
from Error import AccessError
from auth import auth_register
from channel import channels_create, channel_join
from tools import getData

def test_channel_join_test1():
    ''' test channel join '''
    data = getData()
    authRegisterDict = auth_register("channeljoin@ad.unsw.edu.au", "123456", "channel", "join")
    token = authRegisterDict['token']
    #set up user2
    authRegisterDict = auth_register("channel@join.unsw.edu.au", "123456", "channel", "cannotjoin")
    token2 = authRegisterDict['token']
    u_id2 = authRegisterDict['u_id']
    #get two channelId
    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']
    channelsCreateDict = channels_create(token2, 'Channel1', False)
    channelId2 = channelsCreateDict['channel_id']
    #set up finish
    with pytest.raises(ValueError):
        assert channel_join(token, 3707)

    with pytest.raises(AccessError):
        assert channel_join(token, channelId2)

    channel_join(token2, channelId)
    assert u_id2 in data['channels'][channelId]['members']
