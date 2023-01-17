from flask import jsonify

# Handler
def handler(request):
    return jsonify({'status': 'success'}), 200
