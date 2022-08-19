from flask import Flask, jsonify, send_from_directory
from random import randint

# Create Flask app
app = Flask(__name__)

# Constant variable; to track for random rev images
NUM_REVS = 10

# Root route
@app.route("/", methods=['GET'])
def root():
    # Turn Python dict into JSON
    return jsonify({'text': 'Welcome to the Rev API!'})

# <> is used for path parameters
@app.route("/rev/<id>/", methods=['GET'])
def get_rev(id):
    # Sends static file
    return send_from_directory('static/rev/', f'{id}.jpg')

@app.route("/rev/", methods=['GET'])
def get_rev_random():
    # Same as above, just using a random file instead of a specific one
    return send_from_directory('static/rev/', f'{randint(1,NUM_REVS)}.jpg')

@app.errorhandler(404)
def error(err):
    # err parameter tracks error information; This error handler is for 404 (not found)
    return jsonify({'error': 'Rev not found!'})