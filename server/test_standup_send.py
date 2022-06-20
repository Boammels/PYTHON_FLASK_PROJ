''' this is a pytest testing standup_send '''
import pytest
from auth import auth_register
from search import standup_send, standup_start
from channel import channels_create, channel_join
from Error import AccessError

def test_standup_send():
    ''' main tests '''
    #logged in but channel not exist
    the_value_for_the_first_user = auth_register(
        "1212413@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smimth"
    )

    token = the_value_for_the_first_user['token']
    the_value_for_the_second_user = auth_register(
        "13153523@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smimth"
    )
    token2 = the_value_for_the_second_user['token']
    with pytest.raises(ValueError, match=r"*"):
        assert standup_send(token, 1234123, "this is a useless message")

    #logged in, channel exist, but not a member
    channel_value = channels_create(token, "room name", True)
    room_id = channel_value['channel_id']
    with pytest.raises(AccessError, match=r"*"):
        assert standup_send(token2, room_id, "this is a useless message")

    #logged in, channel exist, already a member, valid message
    channel_join(token2, room_id)
    standup_start(token, room_id, 5)
    assert standup_send(token, room_id, "this is a valid message") == {}
    #more than 1000 chars message
    with pytest.raises(ValueError, match=r"*"):
        assert standup_send(token, room_id, "this is a useless message"*100)
