from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
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
blog_posts = dict()
blog_metadata = list()
blog_html = dict()

def initialize_blog(blog_posts: dict, blog_metadata: list, blog_html: dict):
    for post in os.listdir('./blogs'):

        with open(f'./blogs/{post}') as f:
            markdown_content = f.read()

        md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite'])
        output = md.convert(markdown_content)
        meta = md.Meta

        formatter = HtmlFormatter(
            style='github-dark', full=True, cssclass="codehilite")
        css_string = formatter.get_style_defs()
        html = f"<style> {css_string} </style> {output}"

        title = "".join(meta['title'][0])
        date = "".join(meta['date'][0])
        file_name = str(post).replace('.md', '')

        blog_html[file_name] = html

        blog_metadata.append({'name': title,
                           'href': f'{str(post)}', 'date': date, 'file_name': file_name})

        blog_posts[file_name] = ({'name': title,
                           'href': f'{str(post)}', 'date': date, 'file_name': file_name})

    # Sort by most recent
    blog_metadata = sorted(blog_metadata, key=lambda x: x['date'], reverse=True)


initialize_blog(blog_posts, blog_metadata, blog_html)


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
    return templates.TemplateResponse('blog_index.html', {'request': request, 'blog_posts': blog_metadata})


@app.get('/blog/{title}')
async def blog_post(title: str, request: Request):
    if title not in blog_html:
        raise HTTPException(status_code=404, detail=f'Blog with title \"{title}\" not found')

    return templates.TemplateResponse('blog.html', {'request': request, 'html': blog_html[title], 'title': blog_posts[title]['name']})


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
