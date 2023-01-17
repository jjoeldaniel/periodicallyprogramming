from flask import Blueprint, jsonify

# Import app from index.py
from api.index import app

# about_me = Blueprint('about_me', __name__)


@app.route('/api/about_me')
def show():
    return jsonify(
        {
            'name': 'Joel',
            'description': 'Thats me!'
        }), 200
