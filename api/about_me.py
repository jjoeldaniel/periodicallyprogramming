from flask import Blueprint, jsonify

about_me = Blueprint('about_me', __name__)


@about_me.route('/api/about_me')
def show():
    return jsonify(
        {
            'name': 'Joel',
            'description': 'Thats me!'
        }), 200
