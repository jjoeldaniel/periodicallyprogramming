from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    if request.method == 'GET':

        # Get query
        q = request.args.get('query')

        # Check if query is empty
        if q == None:
            return 'Query is empty', 400

        if q == 'projects':

            return jsonify([
                {
                    'name': 'Discord Bot',
                    'description': 'Multi-purpose Discord bot '
                },
                {
                    'name': 'Genius API Wrapper',
                    'description': 'Python wrapper for Genius API '
                },
                {
                    'name': 'Genius API Wrapper',
                    'description': 'A Discord bot meant to integrate with your Canvas class! '
                }

            ])

    # Throw error 405
    else:
        return 'Method not allowed', 405