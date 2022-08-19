from flask import Flask, jsonify, send_from_directory, redirect
from random import randint

app = Flask(__name__)

NUM_REVS = 10

@app.route("/", methods=['GET'])
def root():
    return jsonify({'text': 'Welcome to the Rev API!'})

@app.route("/rev/<id>/", methods=['GET'])
def get_rev(id):
    return send_from_directory('static/rev/', f'{id}.jpg')

@app.route("/rev/", methods=['GET'])
def get_rev_random():
    return send_from_directory('static/rev/', f'{randint(1,NUM_REVS)}.jpg')

@app.errorhandler(404)
def error(err):
    return jsonify({'error': 'Rev not found!'})