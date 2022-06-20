''' test channel leave '''
import pytest
from auth import auth_register
from channel import channels_create, channel_leave
from tools import getData

def test_channel_leave1():
    ''' test channel leave '''
    data = getData()
    authRegisterDict = auth_register("121323123434@ad.unsw.edu.au", "123456", "biuce", "cabyie")
    token = authRegisterDict['token']
    u_id = authRegisterDict['u_id']
    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']

    with pytest.raises(ValueError):
        channel_leave(token, 55667789)
    assert u_id in data['channels'][channelId]['members']
    assert u_id in data['channels'][channelId]['owner']
    channel_leave(token, channelId)
    assert u_id not in data['channels'][channelId]['members']
    assert u_id not in data['channels'][channelId]['owner']
