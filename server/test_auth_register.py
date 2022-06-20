''' test auth register '''
import pytest
import Error
from auth import auth_register

def test_auth_register():
    ''' test auth register '''
    with pytest.raises(ValueError, match=r"*"):
        # Invalid Email
        auth_register("iloveu.com", "123456", "happy", "trump")
    with pytest.raises(ValueError, match=r"*"):
        #Invalid firstname
        auth_register("ilove@u.com", "1234567",
        "123456789012345678901234567890123456789012345678901234567890", "trump")
    with pytest.raises(ValueError, match=r"*"):
        #Invalid lastname
        auth_register("ilove@u.com", "1234567",
        "abc", "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij")
    with pytest.raises(ValueError, match=r"*"):
        #Invalid password
        auth_register("good@email.com", "1234", "happy", "trump")
    registerdict = auth_register("authregister@first.com", "123456", "happy", "trump")
    assert registerdict['token'] != None
    # Correct case
    assert registerdict['u_id'] > -1
    # Previously used email is invalid
    with pytest.raises(ValueError, match=r"*"):
        auth_register("authregister@first.com", "password", "sidene", "sydney")  
