''' this is a pytest for testing users_all function '''
from user_profile import users_all, userprof, user_profile_sethandle
from auth import auth_register

def test_users_all():
    ''' main test '''
    value_for_the_first_user = auth_register(
        "23123dress@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smith"
    )
    token1 = value_for_the_first_user['token']
    u_id1 = value_for_the_first_user['u_id']
    user_profile_sethandle(
        value_for_the_first_user['token'],
        "nice00handle"
    )

    value_for_the_second_user = auth_register(
        "z23255555@ad.unsw.edu.au",
        "C0UR4G3asd",
        "First",
        "Last"
    )
    token2 = value_for_the_second_user['token']
    u_id2 = value_for_the_second_user['u_id']

    user1 = userprof(token1, u_id1)
    user2 = userprof(token2, u_id2)
    result = users_all(token1)

    assert user1 in result['users']
    assert user2 in result['users']
