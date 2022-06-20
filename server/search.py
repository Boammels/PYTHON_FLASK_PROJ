''' functions for search and standup '''
from datetime import timezone
import datetime
from threading import Thread
from tools import getData, getUserFromToken, validUser

from Error import AccessError


def channel_exist(database, channel_id):
    ''' checking if a channel exists '''
    if channel_id >= len(database['channels']):
        return False
    if channel_id < 0:
        return False
    return True

def in_the_channel(u_id, channel):
    ''' check if a user is in a channel '''
    if u_id in channel['members']:
        return True
    return False

def timer(database, channel):
    ''' a timer tool '''
    while (datetime.datetime.utcnow().replace(tzinfo=timezone.utc).timestamp() < channel['stadupEndtime']):
        continue
    channel['standup'] = False
    new_message = {
        'u_id': int(channel['standupby']),
        'channelId': int(channel['channelId']),
        'message_id': len(database['messages']),
        'message': channel['standupMessage'],
        'time_created': datetime.datetime.utcnow().replace(tzinfo=timezone.utc).timestamp(),
        'send_later': None,
        'react': [],
        'is_pinned': False
    }
    # Iinsert at the end of the list, list of messages will be stored in order of
    # message_id. Frontend will handle displaying the messages in the correct
    # order
    database['messages'].append(new_message)
    channel['standupMessage'] = ""

####################################################################################
####################################################################################

def searchMessage(token, query_str):
    ''' function search '''
    data = getData()
    result = {'messages':[]}
    request_user = getUserFromToken(token)
    if validUser(request_user, len(data['users'])):
        for message in data['messages']:
            if query_str in message['message']:
                if request_user in data['channels'][message['channelId']]['members']:
                    curr_message = {
                        'message_id': int(message['message_id']),
                        'u_id': int(message['u_id']),
                        'message': message['message'],
                        'time_created': message['time_created'],
                        'reacts': message['react'],
                        'is_pinned': message['is_pinned']
                    }
                    result['messages'].append(curr_message)
    return result

def standup_active(token, channel_id):
    ''' to check if a standup is active '''
    data = getData()
    request_user = getUserFromToken(token)
    if not validUser(request_user, len(data['users'])):
        raise AccessError("This user is not authorised")
    channel = data['channels'][int(channel_id)]
    # All info required for this function is stored within a channel
    # standup is a boolean which is True when a standup is active
    # standupEndtime is a unix timestamp which stores None if a standup isnt active
    return {
        'is_active': channel['standup'],
        'time_finish': channel['standupEndtime']
    }

def standup_start(token, channel_id, length):
    ''' start a standup '''
    # Channel id and length passed in as ints to the server
    data = getData()
    if not channel_exist(data, channel_id):
        raise ValueError("Channel does not exist")
    channel = data['channels'][channel_id]
    request_user = getUserFromToken(token)
    if not in_the_channel(request_user, channel):
        raise AccessError("User who requested standup is not a member of this channel")
    if channel['standup']:
        raise ValueError("Another standup is already running")
    endtime = (datetime.datetime.utcnow()+datetime.timedelta(seconds=length)).replace(tzinfo=timezone.utc).timestamp()
    channel['stadupEndtime'] = endtime
    channel['standup'] = True
    channel['standupby'] = request_user
    Thread(target=timer, args=(data, channel)).start()
    return {'time_finish': endtime}

def standup_send(token, channel_id, message):
    ''' send a message while standup '''
    # Channel id is an int
    data = getData()
    if not channel_exist(data, channel_id):
        raise ValueError("Channel does not exist")
    channel = data['channels'][channel_id]
    request_user = getUserFromToken(token)
    if not in_the_channel(request_user, channel):
        raise AccessError("User who requested standup is not a member of this channel")
    if not channel['standup']:
        raise ValueError("Standup is not currently on in this channel")
    if len(message) > 1000:
        raise ValueError("Message too long")
    username = data['users'][request_user]['handle']
    channel["standupMessage"] += username + ": " + message + "\n"
    return {}
