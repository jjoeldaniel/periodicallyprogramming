from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='../templates', static_folder='../static')

args = ['query']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():

    # Check if request is empty
    if request.args is None:
        return jsonify(
            {'status:' '400'},
            {'error': 'No arguements provided'}), 400

    # Check if all arguements are valid and return 400 if not
    for arg in list(request.args.keys()):
        if arg not in args:
            return jsonify(
                {'status': '400'},
                {'error': 'Invalid arguement provided'}), 400

    if request.method == 'GET':

        # Get query
        q = request.args.get('query')

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

            ], 200)
        
        else:
            return jsonify(
                {'status': '400'},
                {'error': 'Invalid query provided'}), 400

    # Throw error 405
    return jsonify(
                {'status': '405'},
                {'error': 'Method not allowed'}), 405