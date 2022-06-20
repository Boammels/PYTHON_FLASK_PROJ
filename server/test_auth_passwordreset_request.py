''' Test auth password reset request. '''
import pytest
from auth import auth_password_request, auth_register

def test_auth_passwordreset_request():
    ''' Test auth password reset request. '''
    #Not registered
    with pytest.raises(ValueError, match=r"*"):
        assert auth_password_request("ilove@u.com")

    registerdict = auth_register("resetrequest@first.com", "123456", "happy", "trump")
    assert type(registerdict) == dict
    #registered
    result = auth_password_request("resetrequest@first.com")
    assert result == {}
