from flask import *
import json, time

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')
