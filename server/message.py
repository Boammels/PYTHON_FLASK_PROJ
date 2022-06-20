''' This file handles message commands '''

import datetime
from datetime import timezone
#import time
from threading import Thread
from tools import *
from Error import AccessError

def getChannel(channel_id):
    '''Returns the channel if it is exists, if not returns -1.'''
    try:
        return data['channels'][int(channel_id)]
    except:
        return -1

def userInChannel(u_id, channel):
    '''Function to check if a user is in a given channel.'''
    for user in channel['members']:
        if int(user) == int(u_id):
            return 1
    return 0

def getValidMessage(message_id, token_user):
    '''Finds a message given it's message_id.'''
    if token_user == -1:
        raise ValueError("invalid user")
    for msg in data['messages']:
        if int(msg['message_id']) == int(message_id):
            return msg
    raise ValueError("Invalid message")

def isOwner(user, channel_id):
    ''' Simple function which given a users u_id checks if they are an
    owner of that channel.'''
    for channel in data['channels']:
        if int(channel['channelId']) == int(channel_id):
            for owner in channel['owner']:
                if int(owner) == int(user):
                    return 1
            break
    return 0

def timer(data, new_message):
    ''' This timer is used for send message later, could be reused for when
    we implement standup as it requires similar features. '''
    while (datetime.datetime.utcnow().replace(tzinfo=timezone.utc).timestamp() < new_message['send_later']):
        continue
    data['messages'].append(new_message)

def checkValidChannelandUser(data, u_id, current_channel):
    ''' Performs checks to see whether the user and channel are valid. '''
    # Check the user is valid
    if u_id == -1:
        raise ValueError("Invalid user")
    #check channel exist
    if current_channel == -1:
        raise ValueError("Channel does not exist")
    #Check the user is in the channel
    if userInChannel(u_id, current_channel) == 0:
        raise AccessError("Cannot send messages in channels you're not in")

########################FUNCTIONS##########################

def message_send(token, channel_id, message):
    ''' Function which sends a message, both storing the sent message in the
    backend and returning the required information about the message to the
    frontend. '''
    data = getData()
    token_user = getUserFromToken(token)
    current_channel = getChannel(channel_id)
    checkValidChannelandUser(data, token_user, current_channel)
    if len(message) > 1000:
        raise ValueError("Message too long")
    new_message = {
        'u_id': token_user,
        'channelId': int(channel_id),
        'message_id': len(data['messages']),
        'message': message,
        'time_created': datetime.datetime.utcnow().replace(tzinfo=timezone.utc).timestamp(),
        'send_later': None,
        'react': [],
        'is_pinned': False
    }
    # Insert at the end of the list, list of messages will be stored in order of
    # message_id. Frontend will handle displaying the messages in the correct
    # order
    data['messages'].append(new_message)
    # Return the message  in the required format
    return {"message_id" : new_message['message_id']}

def message_remove(token, message_id):
    ''' Given a valid user, remove a message from the data '''
    data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    # Check if the user trying to delete the message actually sent it
    if msg['u_id'] == token_user or isOwner(token_user, msg['channelId']) == 1:
        data['messages'].remove(msg)
    else:
        raise AccessError("You did not send this message or are not an owner")
    return {}

def message_sendlater(token, channel_id, message, time_sent):
    ''' Send a message to a given channel at the time passed in. '''
    data = getData()
    token_user = getUserFromToken(token)
    current_channel = getChannel(channel_id)
    checkValidChannelandUser(data, token_user, current_channel)
    if len(message) > 1000:
        raise ValueError("Message too long")
    if float(time_sent) < datetime.datetime.utcnow().replace(tzinfo=timezone.utc).timestamp():
        raise ValueError("Cannot send messages in the past")
    new_message = {
        'u_id': token_user,
        'channelId': int(channel_id),
        'message_id': len(data['messages']),
        'message': message,
        'time_created': float(time_sent),
        'send_later': float(time_sent),
        'react': [],
        'is_pinned': False
    }
    # Threads allow 2 sections of code to execute at the same time
    # The code will stay in this thread until the time has elapsed. Then it will
    # add the message to data to be displayed.
    Thread(target=timer, args=(data, new_message)).start()
    return {"message_id" : new_message['message_id']}

def message_edit(token, message_id, message):
    ''' Given a message and valid user, change that messages text to
    the new text given. '''
    data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    # Check if the user trying to delete the message actually sent it
    if (msg['u_id'] == token_user or isOwner(token_user, msg['channelId']) == 1):
        if message == "":
            message_remove(token, message_id)
        else:
            msg['message'] = message
    else:
        raise AccessError("You cannot edit this message")
    return {}

def message_pin(token, message_id):
    ''' Given a valid user and valid message, mark it as pinned so it has
    special frontend treatment. '''
    data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    current_channel = getChannel(msg['channelId'])
    if msg['is_pinned']:
        raise ValueError("This message is already pinned")
    # Admin and owner are essentially the same thing with the same priveledges.
    # i.e. Owners have administrative power
    if isOwner(token_user, msg['channelId']) == 0 or userInChannel(token_user, current_channel) == 0:
        #User must both be a member of the channel and an admin of it in order
        #to pin messages
        raise ValueError("Unauthorised users cannot pin messages")
    msg['is_pinned'] = True
    return {}

def message_unpin(token, message_id):
    ''' Given a valid message and a valid user, unpin a pinned message. '''
    data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    current_channel = getChannel(msg['channelId'])
    if msg == -1:
        raise  ValueError("Invalid message_id")
    if not msg['is_pinned']:
        raise ValueError("This message is already unpinned")
    # Admin and owner are essentially the same thing with the same priveledges.
    # i.e. Owners have administrative power
    if isOwner(token_user, msg['channelId']) == 0 or userInChannel(token_user, current_channel) == 0:
        #User must both be a member of the channel and an admin of it in order
        #to pin messages
        raise ValueError("Unauthorised users cannot unpin messages")
    msg['is_pinned'] = False
    return {}

def message_react(token, message_id, react_id):
    ''' Given a message, set it as reacted to by a certain user on the backend
    frontend handles the display. '''
    #data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    current_channel = getChannel(msg['channelId'])
    if userInChannel(token_user, current_channel) == 0:
        raise AccessError("Cannot react to messages in channels you're not in")
    prevReact = 0
    # This code handles multiple react_id's even though right now, there is only
    # a thumbs up react with id 1.
    for react in msg['react']:
        if int(react['react_id']) == int(react_id):
            prevReact = 1
            currReact = react
            break
    if prevReact == 0:
        new_react = {
            'react_id': int(react_id),
            'u_ids': [token_user],
            'is_this_user_reacted': True
        }
        msg['react'].append(new_react)
    else:
        if token_user not in currReact['u_ids']:
            currReact['u_ids'].append(token_user)
            currReact['is_this_user_reacted'] = True
        else:
            raise ValueError("You have already reacted in this way to this message")
    return {}

def message_unreact(token, message_id, react_id):
    ''' Unreact to a mesage that a given user has previously reacted to. '''
    data = getData()
    token_user = getUserFromToken(token)
    msg = getValidMessage(message_id, token_user)
    current_channel = getChannel(msg['channelId'])
    if userInChannel(token_user, current_channel) == 0:
        raise AccessError("Cannot react to messages in channels you're not in")
    valid = 0
    for react in msg['react']:
        if (token_user in react['u_ids']) and (int(react['react_id']) == int(react_id)):
            valid = 1
    if valid == 0:
        raise ValueError("Cannot unreact to a message you have not reacted to")
    for react in msg['react']:
        if int(react['react_id']) == int(react_id):
            react['u_ids'].remove(token_user)
            react['is_this_user_reacted'] = False
    return {}
