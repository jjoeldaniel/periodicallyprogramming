from flask import Blueprint, jsonify
from http.server import BaseHTTPRequestHandler

about_me = Blueprint('about_me', __name__)


@about_me.route('/api/about_me')
def show():
    return jsonify(
        {
            'name': 'Joel',
            'description': 'Thats me!'
        }), 200

# Handler
def handler(request):
    return about_me(request)
