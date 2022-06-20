''' this is a pytest testing standup_start function '''
import datetime
from datetime import timezone
import pytest
from auth import auth_register
from search import standup_start
from channel import channels_create, channel_join
from Error import AccessError

def test_standup_start():
    ''' main tests '''
    #logged in but channel not exist
    user_value = auth_register("1231232312@gmail.com", "P455W0RDabc", "Jack", "Smimth")
    token = user_value['token']
    user_value = auth_register("12312312@gmail.com", "P455W0RDabc", "Jack", "Smimth")
    token2 = user_value['token']
    with pytest.raises(ValueError, match=r"*"):
        assert standup_start(token, 114214325, 1)

    #logged in, channel exist, but not a member
    channel_value = channels_create(token, "room name", True)
    room_id = channel_value['channel_id']
    with pytest.raises(AccessError, match=r"*"):
        assert standup_start(token2, room_id, 5)

    #logged in, channel exist, already a member, valid message
    channel_join(token2, room_id)
    endtime = (datetime.datetime.utcnow()+datetime.timedelta(seconds=5)).replace(tzinfo=timezone.utc).timestamp()
    result = standup_start(token, room_id, 5)
    # int handles accuracy not being entirely perfect
    assert int(result['time_finish']) == int(endtime)
