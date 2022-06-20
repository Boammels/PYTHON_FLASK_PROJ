'''Test channel details'''
import pytest
from Error import AccessError
from auth import auth_register
from channel import channels_create, channel_details, channel_join

def test_channel_details1():
    '''Test channel details'''
    user1 = auth_register("the_first@details.com", "123124", "wdawda", "awgawfge")
    token1 = user1['token']
    u_id1 = user1['u_id']
    user2 = auth_register("the_e@details.com", "123124", "wdawda", "awgawfge")
    token2 = user2['token']
    u_id2 = user2['u_id']
    user3 = auth_register("the_fafcwe@details.com", "123124", "wdawda", "awgawfge")
    token3 = user3['token']
    channel = channels_create(token1, "detail_channel", True)
    channel_id = channel['channel_id']
    channel_join(token2, channel_id)
    with pytest.raises(ValueError, match=r"*"):
         #channel not exist
        assert channel_details(token1, 1246)
    with pytest.raises(AccessError, match=r"*"):
        # Not a member
        assert channel_details(token3, channel_id)
    result = channel_details(token1, channel_id)
    assert result == {'name': "detail_channel", 'owner_members': [{
        'u_id': u_id1,
        'name_first': "wdawda",
        'name_last': "awgawfge",
        'profile_img_url': "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
    }], 'all_members':[{
        'u_id': u_id1,
        'name_first': "wdawda",
        'name_last': "awgawfge",
        'profile_img_url': "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
    }, {
        'u_id': u_id2,
        'name_first': "wdawda",
        'name_last': "awgawfge",
        'profile_img_url': "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
    }]}
