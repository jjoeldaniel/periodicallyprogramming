from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Register blueprints
# app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')