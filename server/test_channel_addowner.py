''' Test channel owner '''
import pytest
from Error import AccessError
from auth import auth_register
from channel import channel_addowner, channels_create
from tools import getData

def test_channel_addowner_test1():
    ''' Test channel owner '''
    data = getData()
    authRegisterDict = auth_register("z3456782@ad.unsw.edu.au", "123456",
                                     "bob", "Hayden")
    token = authRegisterDict['token']
    u_id1 = authRegisterDict['u_id']
    #set up user2
    authRegisterDict2 = auth_register("z5356782@ad.unsw.edu.au", "129456",
                                      "Tom", "Hiddleson")
    u_id2 = authRegisterDict2['u_id']

    with pytest.raises(ValueError, match=r"*"):
        assert channel_addowner(token, -1, u_id1)                         #channel not exist

    authRegisterDict3 = auth_register("z9956782@ad.unsw.edu.au", "129756",
                                      "Ray", "Wilson")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']

    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']

    # success one
    assert channel_addowner(token, channelId, u_id2) == {}
    assert u_id2 in data['channels'][channelId]['owner']

    with pytest.raises(ValueError, match=r"*"):
        # Already an owner
        assert channel_addowner(token, channelId, u_id1)

    with pytest.raises(AccessError, match=r"*"):
        #token3 is not a owner of a channel
        assert channel_addowner(token3, channelId, u_id3)
