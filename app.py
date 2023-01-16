from flask import *
import json, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

