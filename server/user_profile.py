''' functions for implementing user functionalities '''
import urllib
import requests
from PIL import Image
from tools import getData, getUserFromToken, check_email, validUser
from Error import AccessError

def change_value(data, u_id, feature, value):
    ''' change the value of the feature for the user '''
    user = data['users'][u_id]
    user[feature] = value

def have_duplicate(data, feature, value):
    ''' checking if any other user has already used this value in this feature '''
    for user in data['users']:
        if value == user[feature]:
            return True
    return False

def valid_length(string, mini, maxi):
    ''' checking if a string is within the length provided '''
    if len(string) < mini:
        return False
    if len(string) > maxi:
        return False
    return True

def get_http_status(url):
    ''' checking if the url could respond well '''
    try:
        respond = requests.head(url)
        return respond.status_code == 200
    except requests.ConnectionError:
        return False

def is_url_jpg(image_url):
    ''' checking if the provided url would indicate to a jpg file '''
    image_formats = ["image/jpeg", "image/jpg"]
    respond = requests.head(image_url)
    if respond.headers["content-type"] in image_formats:
        return True
    return False

def save_image(data, u_id, url):
    ''' retrieving the image from web '''
    user_handle = data['users'][u_id]['handle']
    filename = user_handle + "profphoto" + '.jpg'
    path = "./static/"
    urllib.request.urlretrieve(url, path+filename)
    return filename

def check_crop_image_valid(filename, x_start, y_start, x_end, y_end):
    ''' checking if the image is valid to be cropped '''
    path = "./static/"
    image = Image.open(path + filename)
    width, height = image.size
    if int(x_end) <= int(x_start) or int(y_end) <= int(y_start):
        return False
    if int(x_start) < 0 or int(y_start):
        return False
    if int(x_end) > int(width) or int(y_end) > int(height):
        return False
    return True

def crop_image(filename, x_start, y_start, x_end, y_end):
    ''' cropping the image with the dimention provided '''
    path = "./static/"
    image = Image.open(path+filename)
    coords = (int(x_start), int(y_start), int(x_end), int(y_end))
    crpdim = image.crop(coords)
    crpdim.save(path+filename)

def generate_user_profile(user):
    ''' returning the specific user's profile '''
    return {
        'u_id': user['u_id'],
        'email': user['email'],
        'name_first': user['name_first'],
        'name_last': user['name_last'],
        'handle_str': user['handle'],
        'profile_img_url': user['profile_photo']
    }

#####################################################
# Main Functions                                    #
#####################################################

def userprof(token, u_id):
    ''' generating specific user's profile '''
    data = getData()
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        if not validUser(int(u_id), len(data['users'])):
            raise ValueError("User not found")
        user = data['users'][int(u_id)]
        result = generate_user_profile(user)
        return result
    raise AccessError("Token invalid")

def users_all(token):
    ''' generating all users profile '''
    data = getData()
    request_user = getUserFromToken(token)
    if not validUser(request_user, len(data['users'])):
        raise AccessError("User not valid")
    return_users = []
    for user in data['users']:
        a_user = generate_user_profile(user)
        return_users.append(a_user)
    return {'users':return_users}

def user_profile_setname(token, name_first, name_last):
    ''' changing the user's name '''
    data = getData()
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        if not valid_length(name_first, 1, 50) or not valid_length(name_last, 1, 50):
            raise ValueError("First/Last name is too long/short")
        change_value(data, request_user, 'name_first', name_first)
        change_value(data, request_user, 'name_last', name_last)
        return {}
    raise AccessError("Token invalid")

def user_profile_setemail(token, email):
    ''' changing the user's email '''
    data = getData()
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        if have_duplicate(data, 'email', email):
            raise ValueError("Email already used")
        if not check_email(email):
            raise ValueError("Email format is not correct")
        change_value(data, request_user, 'email', email)
        return {}
    raise AccessError("Token invalid")

def user_profile_sethandle(token, handle_str):
    ''' changing the user's handle '''
    data = getData()
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        if have_duplicate(data, 'handle', handle_str):
            raise ValueError("Handle already used")
        if not valid_length(handle_str, 3, 20):
            raise ValueError("Handle too long/short")
        change_value(data, request_user, 'handle', handle_str)
        return {}
    raise AccessError("Token invalid")

def user_profiles_uploadphoto(token, url, x_start, y_start, x_end, y_end, root):
    ''' changing the user's profile photo '''
    data = getData()
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        if not get_http_status(url):
            raise ValueError("The url returns a Http status other than 200")
        if is_url_jpg(url):
            name = save_image(data, request_user, url)
            if check_crop_image_valid(name, x_start, y_start, x_end, y_end):
                crop_image(name, x_start, y_start, x_end, y_end)
                new_url = root +"static/"+name
                #new_url = "http://127.0.0.1:8003/prebundle/static/"+name
                print(new_url)
                change_value(data, request_user, 'profile_photo', new_url)
            else:
                raise ValueError("The dimemsion is out of range")
        else:
            raise ValueError("This url returns a non-jpg result")
    else:
        raise AccessError("Token invalid")
    return {}
