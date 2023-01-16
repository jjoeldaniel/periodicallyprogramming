from flask import *
import json, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('<path:path>')
def catch_all(path):
    return render_template('index.html')