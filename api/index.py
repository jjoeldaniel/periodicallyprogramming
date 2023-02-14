from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/github')
@app.route('/gh')
def github():
    return redirect('https://github.com/jjoeldaniel')


@app.route('/resume')
def resume():
    return redirect('https://www.periodicallyprogramming.com/static/resume.pdf')


@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/joeldanielrico')


@app.route('/project')
@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/api/ping')
def api():
    return jsonify({'status': 'success'}), 200
