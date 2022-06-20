''' test channels create '''
import pytest
import jwt
from Error import AccessError
from auth import auth_register
from channel import channels_create

def test_channel_create():
    ''' test channels create '''
    #set up
    authRegisterDict = auth_register("channel@create.unsw.edu.au", "123456", "Hayden", "Smith")
    token = authRegisterDict['token']
    #set up finish
    invalidtoken = jwt.encode({'u_id': -2, 'name': 'left'}, 'H11A-JBLs', algorithm='HS256')
    with pytest.raises(AccessError):
        assert channels_create(invalidtoken, 'channel', True)
    # Name too long
    with pytest.raises(ValueError):
        assert channels_create(token, 'channnnnnneeeeeelllllll', True)

    reVal = channels_create(token, 'channel1', True)
    assert reVal['channel_id'] > -1
