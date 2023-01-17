from flask import Flask, render_template, jsonify

# Vercel imports require the leading directory for this to work
# Assume all imports are relative to the root of the project
from api.about_me import about_me

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.register_blueprint(about_me)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ping')
def api():
    return jsonify({'status': 'success'}), 200
