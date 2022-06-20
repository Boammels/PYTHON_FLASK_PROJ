''' this is a pytest testing user_profile_setemail function '''
import pytest
from user_profile import user_profile_setemail, userprof
from auth import auth_register

def test_user_profile_setemail():
    ''' pytest function '''
    #loggedin and incorrect email
    value_for_the_first_user = auth_register(
        "123@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smimth"
    )
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setemail(value_for_the_first_user['token'], "incorrectemail")

    #loggedin and correct email
    assert user_profile_setemail(value_for_the_first_user['token'], "correct@email.com") == {}
    assert userprof(
        value_for_the_first_user['token'],
        value_for_the_first_user['u_id']
    )['email'] == 'correct@email.com'

    #new user with duplicate email
    value_for_the_second_user = auth_register("new@email.com", "NEWP455word", "John", "Nobody")
    with pytest.raises(ValueError, match=r"*"):
        assert user_profile_setemail(value_for_the_second_user['token'], "correct@email.com")
