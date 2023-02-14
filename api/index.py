from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api/ping')
def api():
    return jsonify({'status': 'success'}), 200
