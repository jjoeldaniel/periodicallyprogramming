from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
import os

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")


# Get all files and sort by most recently modified
posts = list()
for post in os.listdir('./blogs'):
    posts.append(post)
posts = sorted(posts, key=lambda f: os.path.getmtime(os.path.join('./blogs', f)), reverse=True)

# Build list of file metadata
blog_posts = list()
for post in posts:
    blog_posts.append({'name': f'{str(post).replace(".md", "").replace("_", " ")}',
                 'href': f'{str(post)}', 'file_name': f'{str(post).replace(".md", "")}'})


@app.get('/index', response_class=HTMLResponse)
@app.get('/home', response_class=HTMLResponse)
@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    """Our default routes of '/' and '/index'
    Return: The content we want to display to a user
    """

    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/blog', response_class=HTMLResponse)
async def blog_index(request: Request):
    return templates.TemplateResponse('blog_index.html', {'request': request, 'blog_posts': blog_posts})


@app.get('/blog/{title}')
async def blog_post(title: str, request: Request):
    blog_posts = [str(post) for post in os.listdir('./blogs')]

    if str(title)+".md" not in blog_posts:
        return RedirectResponse(url='/blog')

    with open(f'./blogs/{title}.md') as f:
        markdown_content = f.read()

    md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])
    output = md.convert(markdown_content)
    meta = md.Meta
    print(meta)

    formatter = HtmlFormatter(
        style='github-dark', full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    html = f"<style> {css_string} </style> {output}"

    return templates.TemplateResponse('blog.html', {'request': request, 'html': html, 'title': meta['title'][0]})


@app.get('/about', response_class=HTMLResponse)
@app.get('/contact', response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse('contact.html', {'request': request})


@app.get('/project', response_class=HTMLResponse)
@app.get('/projects', response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse('projects.html', {'request': request})


@app.get('/github')
async def github():
    return RedirectResponse(url='https://github.com/jjoeldaniel')


@app.get('/resume')
async def resume():
    return RedirectResponse(url='https://www.periodicallyprogramming.com/static/resume.pdf')


@app.get('/source')
async def source():
    return RedirectResponse(url='https://github.com/jjoeldaniel/periodicallyprogramming')


@app.get('/linkedin')
async def linkedin():
    return RedirectResponse(url='https://www.linkedin.com/in/joeldanielrico')


@app.get('/*')
async def catch_all():
    return RedirectResponse(url="/home")


if __name__ == '__main__':
    app.run()
