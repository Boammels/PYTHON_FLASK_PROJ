from tools import getUserFromToken, getData
from Error import AccessError

# Should be 50, can be changed for testing
PAGINATION = 50

def generateChannelId(data):
    ''' Generates a channel id '''
    return len(data['channels'])

def checkValidUser(u_id):
    ''' Checks is a user is valid '''
    if u_id == -1:
        raise ValueError("Invalid user")

def doesChannelExist(channel_id):
    ''' checks if the channel exists '''
    data = getData()
    valid = 0
    for channel in data['channels']:
        if channel['channelId'] == channel_id:
            valid = 1
    return valid

def getMemberDict(data, u_id):
    ''' Puts data into the correct form for member required by frontend '''
    u_id = int(u_id)
    memberDict = {
        'u_id': u_id,
        'name_first': data['users'][u_id]['name_first'],
        'name_last': data['users'][u_id]['name_last'],
        'profile_img_url': data['users'][u_id]['profile_photo']
    }
    return memberDict

########################### FUNCTIONS ################################
def channel_invite(channel_id, token, u_id):
    ''' channel invite '''
    data = getData()
    u_id_owner = getUserFromToken(token)
    checkValidUser(u_id_owner)
    #check channel exist
    if doesChannelExist(channel_id) == 0:
        raise ValueError("channel not exists")
    if int(u_id) >= len(data['users']):
        raise ValueError("Target user does not exist")
    #check if token is a member of this channel
    channel = data['channels'][channel_id]
    if u_id in channel['members']:
        raise AccessError("user already in this channel")
    if u_id_owner not in channel['members']:
        raise AccessError("Not a member of channel, cannot add others")
    if data['users'][u_id]['permission_id'] in [1, 2]:
        channel['owner'].append(u_id)
    channel['members'].append(u_id)
    return {}

def channel_details(token, channel_id):
    ''' channel details '''
    data = getData()
    auth_user = getUserFromToken(token)
    checkValidUser(auth_user)
    if doesChannelExist(channel_id) == 0:
        raise ValueError("Channel does not exist")
    channel = data['channels'][channel_id]
    if auth_user not in channel['members']:
        raise AccessError("This user is not authorized to check the detail of this channel")
    # Member data must be given to the server in the following format:
    # List of dictionaries containing u_id, name_first and name_last as per the spec.
    # The function getMemberDict(data, u_id) handles this.
    channel_members = []
    for mem in channel['members']:
        channel_members.append(getMemberDict(data, mem))
    channel_owners = []
    for owner in channel['owner']:
        channel_owners.append(getMemberDict(data, owner))
    return {
        'name' : channel['name'],
        'owner_members' : channel_owners,
        'all_members' : channel_members
    }

def channel_messages(token, channel_id, start):
    ''' channel messages '''
    data = getData()
    auth_user = getUserFromToken(token)
    checkValidUser(auth_user)
    if doesChannelExist(channel_id) == 0:
        raise ValueError("Channel does not exist")
    channel = data['channels'][channel_id]
    if auth_user not in channel['members']:
        raise AccessError("Not a member of channel")

    # Get all the messages from the specified channel
    channel_messages = []
    count = 0
    for message in data['messages']:
        #print("checking" + str(count))
        if int(message['channelId']) == int(channel_id):
            channel_messages.insert(0, message)
            count += 1
    if start > count:
        raise ValueError("Start is greater than the total number of message of in the channnel")

    return_messages = []
    i = start
    #print("i: " + str(i))
    #print("count: " + str(count))
    while i < (start + PAGINATION) and i < count:
        #All messages will be stored in accordance with their message_id, i.e.
        #message_id 0 at place 0, message_id 1 at place 1 ect.
        # React will only work for the thumbs up react with id 1
        print(channel_messages[i])
        uReacted = False
        if channel_messages[i]['react'] != []:
            if auth_user in channel_messages[i]['react'][0]['u_ids']:
                uReacted = True
            channel_messages[i]['react'][0]['is_this_user_reacted'] = uReacted
        currMessage = {
            'message_id': int(channel_messages[i]['message_id']),
            'u_id': int(channel_messages[i]['u_id']),
            'message': channel_messages[i]['message'],
            'time_created': channel_messages[i]['time_created'],
            'reacts': channel_messages[i]['react'],
            'is_pinned': channel_messages[i]['is_pinned']
        }
        return_messages.append(currMessage)
        i += 1
    print(return_messages)
    # Five messages have not been given back, then there are no more messages
    # to be displayed. end = -1 indicates no more messages to be displayed.
    if (i - start) != PAGINATION or i == count:
        end = -1
    else:
        end = start + PAGINATION
    return {'messages' : return_messages, 'start' : start, 'end' : end}

def channels_create(token, name, is_public):
    ''' channels create '''
    #channels = getChannel()
    data = getData()
    #use u_id as 'owner'
    new_owner = getUserFromToken(token)
    print(type(new_owner))
    if new_owner == -1:
        raise AccessError("Invalid user")
    #check the length of name
    if len(name) > 20:
        raise ValueError("Invalid channel name")
    newchannel = {}
    newchannel['name'] = name
    newchannel['owner'] = []
    newchannel['owner'].append(int(new_owner))
    newchannel['channelId'] = generateChannelId(data)
    newchannel['privacy'] = is_public
    newchannel['members'] = []
    newchannel['members'].append(int(new_owner))
    newchannel['standup'] = False
    newchannel['standupEndtime'] = None
    newchannel['standupMessage'] = ""
    newchannel['standupby'] = None
    data['channels'].append(newchannel)
    return {'channel_id' : newchannel['channelId']}

def channel_listall(token):
    ''' channel listall '''
    # channels should be output in this form { channel_id, name }
    data = getData()
    user = getUserFromToken(token)
    checkValidUser(user)
    all_channels_list = []
    for channel in data['channels']:
        newChannel = {
            'channel_id': channel['channelId'],
            'name': channel['name']
        }
        all_channels_list.append(newChannel)
    return {'channels' : all_channels_list}

def channel_list(token):
    ''' channel list '''
    data = getData()
    user = getUserFromToken(token)
    checkValidUser(user)
    my_channels_list = []
    for channel in data['channels']:
        #for mem in channel['members']:
        #if mem == user:
        if user in channel['members']:
            newChannel = {
                'channel_id': channel['channelId'],
                'name': channel['name']
            }
            my_channels_list.append(newChannel)
    return {'channels' : my_channels_list}

def channel_join(token, channel_id):
    ''' channel join '''
    # Assume that this function can only be called when the tokened user has accepted
    # a valid invitation
    data = getData()
    user = getUserFromToken(token)
    checkValidUser(user)
    if doesChannelExist(channel_id) == 0:
        raise ValueError("channel does not exist")
    channel = data['channels'][channel_id]
    if not channel['privacy']:
        raise AccessError("channel is not public")
    if user in channel['members']:
        raise AccessError("user already in this channel")
    #If a slackr owner joins, they should have owner access
    if data['users'][user]['permission_id'] in [1, 2]:
        channel['owner'].append(user)
    channel['members'].append(user)
    return {}

def channel_leave(token, channel_id):
    ''' channel leave '''
    data = getData()
    if doesChannelExist(channel_id) == 0:
        raise ValueError("channel does not exist")
    u_id = getUserFromToken(token)
    checkValidUser(u_id)
    channel = data['channels'][channel_id]
    if u_id in channel['members']:
        channel['members'].remove(u_id)
    else:
        # User is not a member
        raise ValueError("User not a member of this channel - cannot leave")
    if u_id in channel['owner']:
        channel['owner'].remove(u_id)
    return {}

def channel_addowner(token, channel_id, u_id):
    ''' channel addowner '''
    #User must already be in channel in order to be made an owner
    #channels = getChannel():
    data = getData()
    u_id_owner = getUserFromToken(token)
    checkValidUser(u_id_owner)
    if doesChannelExist(channel_id) == 0:
        raise ValueError("channel does not exist")
    channel = data['channels'][channel_id]
    if u_id_owner not in channel['owner']:
        raise AccessError("The request user is not an owner of this channel")
    if u_id in channel['owner']:
        raise ValueError("Already the owner of this channel")
    channel['owner'].append(u_id)
    if u_id not in channel['members']:
        channel['members'].append(u_id)
    return {}

def channel_removeowner(token, channel_id, u_id):
    ''' channel removeowner '''
    data = getData()
    rUser = getUserFromToken(token)
    checkValidUser(rUser)
    if doesChannelExist(channel_id) == 0:
        raise ValueError("channel does not exist")
    channel = data['channels'][channel_id]
    if u_id not in channel['owner']:
        raise ValueError("Target not an owner of the channel")
    if rUser not in channel['owner']:
        raise AccessError("The one calling this function is not an owner")
    channel['owner'].remove(int(u_id))
    return {}
