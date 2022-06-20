''' this is a pytest testing searchMessage '''
from auth import auth_register
from channel import channels_create
from message import message_send
from search import searchMessage

def test_search():
    '''
    #not logged in
    l = search("thisisainvalidtoken","searching key words")
    assert check_result("searching key words",l) == True
    '''
    #logging
    user_value = auth_register("test_search@gmail.com", "P455W0RDabc", "Jack", "Smimth")
    token = user_value['token']
    #creating a roomand join the room
    channel_value = channels_create(token, "room name", True)
    room_id = channel_value['channel_id']
    #sending a message
    message_send(token, room_id, "This is a sentence containing searching key words lalalala")
    result = searchMessage(token, "searching key words falalala")["messages"]
    assert result == []
    result = searchMessage(token, "searching key words lalalala")["messages"]
    assert result[0]['message'] == "This is a sentence containing searching key words lalalala"
