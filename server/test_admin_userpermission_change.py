''' Test admin permission change '''
import pytest
from Error import AccessError
from auth import auth_register, admin_userpermission_change

def test_admin_userpermission_change_u_di():
    ''' Test for an invalid u_id. '''
    dic1 = auth_register("ilove11243@u.com", "123456", "happy", "trump")
    token = dic1['token']
    uid = 11111
    with pytest.raises(ValueError, match=r"*"):
        admin_userpermission_change(token, uid, 1)

def test_admin_userpermission_change_permission_id():
    ''' Test for invalid permission id '''
    dic1 = auth_register("ihate@u.com", "123456", "happy", "trump")
    token = dic1['token']
    uid = dic1['u_id']
    with pytest.raises(ValueError, match=r"*"):
        admin_userpermission_change(token, uid, 6)

def test_admin_userpermission_change_correct():
    ''' Test changing permissions higher than '''
    dic1 = auth_register("iown@u.com", "123456", "happy", "trump")
    dic2 = auth_register("iown42212@u.com", "123456", "happy", "trump")
    uid = dic1['u_id']
    token2 = dic2['token']
    with pytest.raises(AccessError, match=r"*"):
        admin_userpermission_change(token2, uid, 3)
