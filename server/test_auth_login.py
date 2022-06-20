''' Test auth login '''
import pytest
from auth import auth_login, auth_register

def test_auth_login_test_invalidemail():
    ''' Test auth login '''
    with pytest.raises(ValueError, match=r"*"):
        auth_login("iloveu.com", "123456")
    with pytest.raises(ValueError, match=r"*"):
        auth_login("ilove@u.com", "123456")

    auth_register("authlogin@test1.com", "password", "happy", "trump")

    with pytest.raises(ValueError, match=r"*"):
        auth_login("authlogin@test1.com", "1234556")
    logindict = auth_login("authlogin@test1.com", "password")
    assert logindict['token']
    assert logindict['u_id'] > -1
