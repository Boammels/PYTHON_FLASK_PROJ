''' this is a pytest testing useprof function '''
import pytest
from user_profile import user_profile_setname, userprof
from auth import auth_register

def test_user_profile_setname():
    ''' function '''
    #loggedin and incorrect name
    value_for_the_user = auth_register("345@gmail.com", "P455W0RDabc", "Jack", "Smimth")
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setname(
            value_for_the_user['token'],
            "123456789012345678901234567890123456789012345678901234567890",
            "Last"
        )
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setname(value_for_the_user['token'], "", "Last")
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setname(
            value_for_the_user['token'],
            "First",
            "123456789012345678901234567890123456789012345678901234567890"
        )
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setname(value_for_the_user['token'], "First", "")
    #loggedin and correct name
    assert user_profile_setname(value_for_the_user['token'], "First", "Last") == {}
    assert userprof(
        value_for_the_user['token'],
        value_for_the_user['u_id']
    )['name_first'] == 'First'
    assert userprof(
        value_for_the_user['token'],
        value_for_the_user['u_id']
    )['name_last'] == 'Last'
