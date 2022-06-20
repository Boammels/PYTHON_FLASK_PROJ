''' Test channel remove owner '''
import pytest
from Error import AccessError
from auth import auth_register
from channel import channels_create, channel_addowner, channel_removeowner
from tools import getData

def test_channel_removeowner_test1():
    ''' Test channel remove owner '''
    data = getData()
    authRegisterDict = auth_register("remove@owner.one.edu.au", "123456", "bob", "Hayden")
    token = authRegisterDict['token']
    u_id1 = authRegisterDict['u_id']

    authRegisterDict2 = auth_register("remove@owner.two.edu.au", "129456", "Tom", "Hiddleson")
    u_id2 = authRegisterDict2['u_id']

    authRegisterDict3 = auth_register("remove@owner.three.edu.au", "129756", "Ray", "Wilson")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']

    channelsCreateDict = channels_create(token, 'NEW', True)
    channelId = channelsCreateDict['channel_id']

    channel_addowner(token, channelId, u_id2)
    channel_removeowner(token, channelId, u_id2)
    # success one
    assert u_id2 not in data['channels'][channelId]['owner']
    with pytest.raises(ValueError, match=r"*"):
        # the channel doesn't exist
        assert channel_removeowner(token, 55667788, u_id1)
    with pytest.raises(AccessError, match=r"*"):
        # the user is not authorised
        assert channel_removeowner(token3, channelId, u_id1) == {}
    #token3 is not an owner of a channel
    # the target is not actually a owner
    with pytest.raises(ValueError, match=r"*"):
        #u_id3 is not an owner of a channel
        assert channel_removeowner(token, channelId, u_id3)
