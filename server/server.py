"""Flask server"""
import sys
from json import dumps
from flask_cors import CORS
from flask import Flask, request
from auth import *
from user_profile import *
from channel import *
from search import *
from message import *
from Error import AccessError

APP = Flask(__name__)
CORS(APP)

@APP.route('/echo/get', methods=['GET'])
def echo1():
    """ Description of function """
    return dumps({
        'echo' : request.args.get('echo'),
    })

@APP.route('/echo/post', methods=['POST'])
def echo2():
    """ Description of function """
    return dumps({
        'echo' : request.form.get('echo'),
    })

@APP.route('/auth/register', methods=['POST'])
def app_auth_register():
    """ Server wrapper function """
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    try:
        result = auth_register(email, password, name_first, name_last)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/auth/login', methods=['POST'])
def app_auth_login():
    """ Server wrapper function """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        result = auth_login(email, password)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    return dumps(result)

@APP.route('/auth/logout', methods=['POST'])
def app_auth_logout():
    """ Server wrapper function """
    token = request.form.get('token')
    return dumps(auth_logout(token))

@APP.route('/auth/passwordreset/request', methods=['POST'])
def app_auth_passwordreset_request():
    """ Server wrapper function """
    user_email = request.form.get('email')
    try:
        result = auth_password_request(user_email)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    return dumps(result)

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def app_auth_password_reset():
    """ Server wrapper function """
    resetCode = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    try:
        result = auth_password_reset(resetCode, new_password)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    return dumps(result)

@APP.route('/user/profile', methods=['GET'])
def app_user_profile():
    """ Server wrapper function """
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    try:
        result = userprof(token, int(u_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/users/all', methods=['GET'])
def app_users_all():
    """ Server wrapper function """
    token = request.args.get('token')
    try:
        result = users_all(token)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/user/profile/setname', methods=['PUT'])
def app_user_profile_setname():
    """ Server wrapper function """
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    try:
        result = user_profile_setname(token, name_first, name_last)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/user/profile/setemail', methods=['PUT'])
def app_user_profile_setemail():
    """ Server wrapper function """
    token = request.form.get('token')
    email = request.form.get('email')
    try:
        result = user_profile_setemail(token, email)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/user/profile/sethandle', methods=['PUT'])
def app_user_profile_sethandle():
    """ Server wrapper function """
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    try:
        result = user_profile_sethandle(token, handle_str)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def app_user_profiles_uploadphoto():
    """ Server wrapper function """
    token = request.form.get('token')
    img_url = request.form.get('img_url')
    x_start = request.form.get('x_start')
    y_start = request.form.get('y_start')
    x_end = request.form.get('x_end')
    y_end = request.form.get('y_end')
    root = request.url_root
    try:
        result = user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end, root)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/invite', methods=['POST'])
def app_channel_invite():
    """ Server wrapper function """
    channel_id = request.form.get('channel_id')
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    try:
        result = channel_invite(int(channel_id), token, int(u_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/details', methods=['GET'])
def app_channel_details():
    """ Server wrapper function """
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    try:
        result = channel_details(token, int(channel_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/messages', methods=['GET'])
def app_channel_messages():
    """ Server wrapper function """
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    try:
        result = channel_messages(token, int(channel_id), int(start))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channels/create', methods=['POST'])
def app_channel_create():
    """ Server wrapper function """
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    try:
        result = channels_create(token, name, is_public)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channels/listall', methods=['GET'])
def app_channel_listall():
    """ Server wrapper function """
    token = request.args.get('token')
    try:
        result = channel_listall(token)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channels/list', methods=['GET'])
def app_channels_list():
    """ Server wrapper function """
    token = request.args.get('token')
    try:
        result = channel_list(token)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/join', methods=['POST'])
def app_channel_join():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    try:
        result = channel_join(token, int(channel_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/leave', methods=['POST'])
def app_channel_leave():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    try:
        result = channel_leave(token, int(channel_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/addowner', methods=['POST'])
def app_channel_addowner():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    try:
        result = channel_addowner(token, int(channel_id), int(u_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/channel/removeowner', methods=['POST'])
def app_channel_removeowner():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    try:
        result = channel_removeowner(token, int(channel_id), int(u_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/send', methods=['POST'])
def app_message_send():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    try:
        result = message_send(token, channel_id, message)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/remove', methods=['DELETE'])
def app_message_remove():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    try:
        result = message_remove(token, message_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/sendlater', methods=['POST'])
def app_message_sendlater():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    try:
        result = message_sendlater(token, channel_id, message, time_sent)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/edit', methods=['PUT'])
def app_message_edit():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    try:
        result = message_edit(token, message_id, message)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/pin', methods=['POST'])
def app_message_pin():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    try:
        result = message_pin(token, message_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/unpin', methods=['POST'])
def app_message_unpin():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    try:
        result = message_unpin(token, message_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/react', methods=['POST'])
def app_message_react():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    try:
        result = message_react(token, message_id, react_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/message/unreact', methods=['POST'])
def app_message_unreact():
    """ Server wrapper function """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    try:
        result = message_unreact(token, message_id, react_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/search', methods=['GET'])
def app_search():
    """ Server wrapper function """
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    try:
        result = searchMessage(token, query_str)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/standup/active', methods=['GET'])
def app_standup_active():
    """ Server wrapper function """
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    try:
        result = standup_active(token, channel_id)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/standup/send', methods=['POST'])
def app_standup_send():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    try:
        result = standup_send(token, int(channel_id), message)
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/standup/start', methods=['POST'])
def app_standup_start():
    """ Server wrapper function """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    length = request.form.get('length')
    try:
        result = standup_start(token, int(channel_id), int(length))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

@APP.route('/admin/userpermission/change', methods=['POST'])
def app_admin():
    """ Server wrapper function """
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    permission_id = request.form.get('permission_id')
    try:
        result = admin_userpermission_change(token, int(u_id), int(permission_id))
    except ValueError as exception:
        return dumps({
            "code": 400,
            "name": "ValueError",
            "message": str(exception),
        }), 400
    except AccessError as exception:
        return dumps({
            "code": 403,
            "name": "AccessError",
            "message": str(exception),
        }), 403
    return dumps(result)

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
