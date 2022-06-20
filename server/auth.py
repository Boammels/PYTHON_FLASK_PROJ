import hashlib
import smtplib
import random
from tools import *
from sendEmail import sendEmail
from Error import AccessError
# pylint3 --disable=C0103,W0621,C0116 auth.py this gets 9+ on pytlint
# disable snake case, docstrings and globals

# Generates the token that is used for user authentication
def generateToken(user):
    token = jwt.encode(user, 'H11A-JBLs', algorithm='HS256')
    return token.decode("utf8")

# Encodes a users password using a hash
def encode(password):
    encodedPassword = hashlib.sha256(password.encode()).hexdigest()
    return encodedPassword

# Reset code will be a random 10 digit number
def generateResetCode():
    resetCode = ""
    for _ in range(10):
        resetCode = resetCode + str(random.randint(0, 9))
    return resetCode

# Generates the handle for a user by concatenating there first and last name
# Measures in place to stop repeated handles.
def generateHandle(fName, lName):
    handle = fName.lower() + lName.lower()
    if len(handle) > 18:
        handle = handle[:18]
    while isHandleUnique(handle) == 0:
        if len(handle) >= 20:
            handle = handle[:19]
        handle = handle + str(random.randint(0, 9))
    print(handle)
    return handle

# Goes through all handles to check if a given handle is unique,
# 1-unique, 0-not unique
def isHandleUnique(handle):
    i = 0
    while i < len(data['users']):
        if data['users'][i]['handle'] == handle:
            return 0
        i += 1
    return 1

########################### FUNCTIONS ################################

def auth_register(email, password, name_first, name_last):
    data = getData()
    ## Exceptions checking
    # Invalid email
    if not check_email(email):
        raise ValueError("Invalid email")
    # Invalid password
    if len(password) < 6:
        raise ValueError("Invalid password")
    # Used email
    for user in data['users']:
        if email == user['email']:
            raise ValueError("Email already used")
    # Invalid firstname
    if len(name_first) < 1 or len(name_first) > 50:
        raise ValueError("Invalid first name")
    # Invalid lastname
    if len(name_last) < 1 or len(name_last) > 50:
        raise ValueError("Invalid last name")
    # Create new user for the backend
    u_id = len(data['users'])
    profileUrl = "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
    new_user = {
        'email': email,
        'password': str(encode(password)),
        'name_first': name_first,
        'name_last': name_last,
        'logged_in': 1,
        'u_id': u_id,
        'handle': generateHandle(name_first, name_last),
        'profile_photo': profileUrl
    }
    # First user who joins the slack is an owner as per the spec
    if u_id == 0:
        new_user['permission_id'] = 1
    else:
        new_user['permission_id'] = 3
    #adding the new user to the database
    data['users'].append(new_user)
    # Assume that once you register you are logged in for that session
    # which can be inferred from the front end requiring a token
    # Generating a token
    token = generateToken(new_user)
    return {"u_id": u_id, "token": token}

def auth_login(email, password):
    data = getData()
    #encoding the password for safety reason
    password = str(encode(password))
    ## searching for the user:
    if not check_email(email):
        #if the email is in incorrect format raise an Value Error
        raise ValueError("Invalid email")
    for user in data['users']:
        #if found a matching email
        if user['email'] == email:
            #if password is correct
            if password == user['password']:
                user['logged_in'] = 1
                #generate a token from this user dictionary
                token = generateToken(user)
                return {'u_id': user['u_id'], "token" : token}
            #if password is not correct
            raise ValueError("Password Incorrect")
    #if no matching email, raise ValueError
    raise ValueError("Email not exists")


def auth_logout(token):
    data = getData()
    u_id = getUserFromToken(token)
    # Check if the token is valid
    if u_id != -1:
        # If it is, set the specified users login flag to 0 to log them off
        sUser = data['users'][u_id]
        if sUser['logged_in'] == 1:
            sUser['logged_in'] = 0
            return {'is_success' : True}
    return {'is_success' : False}

def auth_password_request(email):
    data = getData()
    validEmail = -1
    for user in data['users']:
        if user['email'] == email:
            validEmail = 1
            break
    if validEmail == -1:
        raise ValueError("Email not exists")
    #Create a temporary field for this user called resetCode
    #When entered correctly it will be reset
    user['resetCode'] = generateResetCode()
    # Format of this message is important for else the subject field won't
    # actually be the email subject.
    sendEmail("Subject: Password reset\n\nYour account reset code is: " +
              str(user['resetCode']), email)
    return {}

def auth_password_reset(resetCode, newPassword):
    data = getData()
    for user in data['users']:
        try:
        # Check if the reset code given was an currently active for a user
        # Note: does handle the smaller than 0.0001 percent chance that
        # somehow to identical reset codes are simultaneously valid
            if user['resetCode'] == resetCode:
                if len(newPassword) < 6:
                    raise ValueError("Invalid password, must be longer")
                user['password'] = str(encode(newPassword))
                del user['resetCode']
                return {}
        except:
            continue
    raise ValueError("Reset code incorrect")

def admin_userpermission_change(token, u_id, permission_id):
    #permission_id can be 1, 2 or 3 means(ower of slackr, admin of slackr, normal)
    data = getData()
    u_id_caller = getUserFromToken(token)
    currUser = 0
    for user in data['users']:
        if user['u_id'] == u_id_caller:
            currUser = user
    if currUser == 0:
        raise ValueError("Token not valid")

    # check thre permission_id given by arguments refers to a value permission or not
    if permission_id not in [1, 2, 3]:
        raise ValueError("permission_id does not refer to a value permisssion")
    if u_id > len(data['users']):
        raise ValueError("u_id does not refer to a valid user")
    # check the user is authorised to make changes
    if currUser['permission_id'] == 3:
        raise AccessError("The authorised user is not an admin or owner")
    #Stops admins from giving people owner permissions
    if currUser['permission_id'] > permission_id:
        raise AccessError("Cannot allocate permissions higher than you")
    for user in data['users']:
        if user['u_id'] == u_id:
            user['permission_id'] = permission_id
    return {}
