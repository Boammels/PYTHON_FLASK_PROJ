''' this is a pytest testing user_profiles_uploadphoto function '''
import pytest
from user_profile import user_profiles_uploadphoto, userprof
from auth import auth_register

def test_user_profiles_uploadphoto():
    ''' main tests '''
    x_start = 0
    y_start = 0
    x_end = 300000
    y_end = 300000
    root = "http://www.simon.com/"
    value_for_the_user = auth_register(
        "123@gmail.com",
        "P455W0RDabc",
        "Jack",
        "Smimth"
    )
    #url img_url is returns an HTTP status other than 200.
    with pytest.raises(ValueError, match=r"*"):
        assert user_profiles_uploadphoto(
            value_for_the_user['token'],
            "this.is.a/fake/url",
            x_start,
            y_start,
            x_end,
            y_end,
            root
        )
    #x_start, y_start, x_end, y_end are not within the dimensions of the image at the URL.
    with pytest.raises(ValueError, match=r"*"):
        assert user_profiles_uploadphoto(
            value_for_the_user['token'],
            "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg",
            x_start,
            y_start,
            x_end,
            y_end,
            root
        )
    #x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL.
    x_end = 200
    y_end = 200
    #not a jpg:
    with pytest.raises(ValueError, match=r"*"):
        assert user_profiles_uploadphoto(
            value_for_the_user['token'],
            "https://pbs.twimg.com/profile_images/1102327996281610240/U-j4gnz__400x400.png",
            x_start,
            y_start,
            x_end,
            y_end,
            root
        )
    #is a jpg:
    assert user_profiles_uploadphoto(
        value_for_the_user['token'],
        "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg",
        x_start,
        y_start,
        x_end,
        y_end,
        root
    ) == {}
    user = userprof(value_for_the_user['token'], value_for_the_user['u_id'])
    url = "http://www.simon.com/static/"+user['handle_str']+"profphoto.jpg"
    assert user['profile_img_url'] == url
