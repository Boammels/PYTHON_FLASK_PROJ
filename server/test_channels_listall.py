''' test channels listall '''
from auth import auth_register
from channel import channels_create, channel_listall

def test_channel_listall_test1():
    ''' test channels listall '''
    user1 = auth_register("channels321@list.unsw.edu.au", "123456", "bob", "Hayden")
    token = user1['token']

    authRegisterDict2 = auth_register("channels@list2.unsw.edu.au", "129456", "Tom", "Hiddleson")
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, 'Channel1', True)
    channelId = channelsCreateDict['channel_id']

    channelsCreateDict2 = channels_create(token2, 'Channel2', True)
    channelId2 = channelsCreateDict2['channel_id']
    reVal = channel_listall(token)
    assert {'channel_id': channelId, 'name': 'Channel1'} in reVal['channels']
    assert {'channel_id': channelId2, 'name': 'Channel2'} in reVal['channels']
