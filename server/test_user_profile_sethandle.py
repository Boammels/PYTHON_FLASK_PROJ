''' this is a pytest testing user_profile_sethandle function '''
import pytest
from user_profile import user_profile_sethandle, userprof
from auth import auth_register

def test_user_profile_sethandle():
    ''' main test '''
    #loggedin and valid handle
    value_for_the_first_user = auth_register("234@gmail.com", "P455W0RDabc", "Jack", "Smimth")
    assert user_profile_sethandle(value_for_the_first_user['token'], "oh nice handle") == {}
    assert userprof(
        value_for_the_first_user['token'],
        value_for_the_first_user['u_id']
    )['handle_str'] == 'oh nice handle'

    #loggedin and too long/ short handle
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_sethandle(
            value_for_the_first_user['token'],
            "this is really a long and bad handle"
        )
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_sethandle(value_for_the_first_user['token'], "xx")

    #new user logged in with duplicate handle
    value_for_the_second_user = auth_register("212334@gmail.com", "P455W0RDabc", "Jack2", "Smimth")
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_sethandle(value_for_the_second_user['token'], "oh nice handle")
