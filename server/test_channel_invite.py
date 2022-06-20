''' test channel invite '''
import pytest
from Error import AccessError
from auth import auth_register
from channel import channels_create, channel_invite
from tools import getData

def test_channel_invite1():
    ''' test channel invite '''
    #set up
    data = getData()
    authRegisterDict = auth_register("1234@ad.unsw.edu.au", "123456", "ASK", "Sadsamith")
    token1 = authRegisterDict['token']
    u_id1 = authRegisterDict['u_id']

    authRegisterDict = auth_register("5678@ad.unsw.edu.au", "123456", "Is", "Very")
    token2 = authRegisterDict['token']
    u_id2 = authRegisterDict['u_id']

    authRegisterDict = auth_register("910JK@ad.unsw.edu.au", "123456", "Handsone", "Nice")
    u_id3 = authRegisterDict['u_id']

    channelsCreateDict = channels_create(token1, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']
    #set up finish
    with pytest.raises(ValueError, match=r"*"):
        assert channel_invite(1214124231, token1, u_id1)

    with pytest.raises(ValueError, match=r"*"):
        assert channel_invite(channelId, token1, "479")

    with pytest.raises(AccessError, match=r"*"):
        assert channel_invite(channelId, token2, u_id3)

    channel_invite(channelId, token1, u_id2)
    assert u_id2 in data['channels'][channelId]['members']
