from flask import Flask, render_template, render_template_string, jsonify, redirect, url_for
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
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
    posts = list()
    for post in os.listdir('./blogs'):
        posts.append({'name': f'{str(post).replace(".md", "").replace("_", " ")}',
                     'href': f'{str(post)}', 'file_name': f'{str(post).replace(".md", "")}'})

    return render_template('blog_index.html', blog_posts=posts, )


@app.route('/blog/<string:title>')
def blog_post(title=None):
    blog_posts = [str(post) for post in os.listdir('./blogs')]

    if str(title)+".md" not in blog_posts:
        return redirect(url_for("blog_index"))

    with open(f'./blogs/{title}.md') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(
        markdown_content,
        extensions=["fenced_code", "codehilite"]
    )

    formatter = HtmlFormatter(
        style='github-dark', full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + html_content

    title = str(title).replace(".md", "").replace("_", " ")
    return render_template('blog.html', title=title, html=md_template)


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
def source():
    return redirect('https://github.com/jjoeldaniel/periodicallyprogramming')


@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/joeldanielrico')


@app.route('/project')
@app.route('/projects')
def projects():
    return render_template('projects.html')


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
