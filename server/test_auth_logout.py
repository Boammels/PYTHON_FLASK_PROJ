''' Test auth logout '''
import pytest
import jwt
from auth import auth_logout, auth_register

def test_auth_logout():
    ''' Test auth logout '''
    result = auth_register("auth_logout@test.com", "123456", "auth", "logout")
    token = result['token']
    output = auth_logout(token)
    assert output == {'is_success': True}
    output = auth_logout(token)
    assert output == {'is_success': False}

    token = jwt.encode({'u_id':123, 'name': 'left'}, 'H11A-JBLs', algorithm='HS256')
    output = auth_logout(token)
    assert output == {'is_success': False}
