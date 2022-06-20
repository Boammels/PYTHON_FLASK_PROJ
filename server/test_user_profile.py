''' this is a pytest testing the userprof function '''
import pytest
from user_profile import userprof, user_profile_sethandle
from auth import auth_register



def test_user_profile():
    ''' function '''
    #valid token but invalid u_id
    value_for_the_first_user = auth_register(
        "aemailaddress@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smith"
    )
    uid = value_for_the_first_user['u_id']
    user_profile_sethandle(value_for_the_first_user['token'], "nice handle")

    value_for_the_second_user = auth_register(
        "z5555555@ad.unsw.edu.au",
        "C0UR4G3asd",
        "First",
        "Last"
    )
    token = value_for_the_second_user['token']
    with pytest.raises(ValueError, match=r"*"):
        assert userprof(token, 123123)
    result = userprof(token, uid)    #all valid
    assert result['email'] == "aemailaddress@gmail.com"
    assert result["name_first"] == "Jack"
    assert result["name_last"] == "Smith"
    assert result["handle_str"] == "nice handle"
