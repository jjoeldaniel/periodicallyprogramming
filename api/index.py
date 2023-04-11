from flask import Flask, render_template, jsonify, redirect, url_for
import os

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    """Our default routes of '/' and '/index'
    Return: The content we want to display to a user
    """

    return render_template('index.html')


@app.route('/blog')
def blog_index():
    blog_posts = [str(post).replace(".md", "") for post in os.listdir('./blogs')]
    return render_template('blog_index.html', blog_posts=blog_posts)


@app.route('/blog/<string:title>')
def blog_post(title=None):
    blog_posts = [str(post).replace(".md", "") for post in os.listdir('./blogs')]

    if title is not None and blog_posts.__contains__(title):
        return "found"

    return "thanks"


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


@app.route('/source')
@app.route('/sourcecode')
@app.route('/source_code')
def source():
    return redirect('https://github.com/jjoeldaniel/periodicallyprogramming')


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


@app.route('/<path:path>')
def catch_all(path):
    """A special route that catches all other requests
    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.
    Return: A redirect to our index route
    """

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
