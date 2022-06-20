from auth import *
import pytest
import tools

'''
assume reset_code is 1000
'''
 

def test_auth_passwordreset_reset():
    register = auth_register("passwordreset@first.com", "123456", "happy", "trump")
    user = register['u_id']
    request = auth_password_request("passwordreset@first.com")
    data = getData()
    resetCode = data['users'][user]['resetCode']
    with pytest.raises(ValueError,match=r"*"):
        auth_password_reset(resetCode, "1235")     # Invalid Password

    with pytest.raises(ValueError,match=r"*"):
        auth_password_reset("1234", "567890")      # Invalid reset code

    output = auth_password_reset(resetCode, "567890") # good  
    encoded = encode("567890")
    assert data['users'][user]['password'] == encoded
    
        
    
