from flask import Blueprint, request

api = Blueprint('api', __name__)

@api.route('/api')
def req():
    user = request.args.get('user')
    return f'Hello {user}'