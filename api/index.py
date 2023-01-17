from flask import Flask, render_template, jsonify, request

# Vercel imports require the leading directory for this to work
# Assume all imports are relative to the root of the project
from api.api import handler

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    return handler(request=request)
