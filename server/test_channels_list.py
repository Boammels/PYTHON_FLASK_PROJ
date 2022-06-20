''' test channels list '''
from auth import auth_register
from channel import channels_create, channel_list

def test_channel_list_test1():
    ''' test channels list '''
    auth_register_dict = auth_register("channel@list1.unsw.edu.au", "123456", "bob", "Hayden")
    token = auth_register_dict['token']

    #set up user2
    auth_register_dict2 = auth_register("channel@list2.unsw.edu.au", "129456", "Tom", "Hiddleson")
    token2 = auth_register_dict2['token']

    channels_create_dict = channels_create(token, 'Channel1', True)
    channelid = channels_create_dict['channel_id']

    channels_create(token2, 'shouldnotbelist', True)
    reval = channel_list(token)
    for channel in reval['channels']:
        assert channel['name'] != 'shouldnotbelist'
    assert reval == {'channels': [{'channel_id': channelid, 'name': 'Channel1'}]}
