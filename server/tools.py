''' this is a file of functions to help '''
import re
import jwt

data = {
    'users' : [],
    'channels':[],
    'messages':[]
}

def getData():
    ''' related to data '''
    global data
    return data

def getUserFromToken(token):
    ''' provide a token and get who the user is '''
    user_prof = jwt.decode(token, 'H11A-JBLs', algorithms=['HS256'])

    u_id = user_prof['u_id']
    for user in data['users']:
        if user['u_id'] == u_id:
            return user['u_id']
    return -1

def check_email(email):
    ''' check if the email is right in format '''
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, str(email))

def validUser(u_id, maxi):
    ''' check if a user is in the list '''
    if int(u_id) < 0:
        return False
    if int(u_id) > int(maxi):
        return False
    else:
        return True
