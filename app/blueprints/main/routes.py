from .import bp as main
from flask import jsonify, request, json
import requests
from app.data import data
from app.result import conference_data

@main.route('/', methods=['GET'])
def index():
    return jsonify(data)

@main.route('/', methods=['POST'])
def result():
    print('Success')
    if json.dumps(conference_data) == request.json['data']:
        return jsonify({'message': 'Success'}), 200
    else:
        print("Oops! Somewhere along the way, you made a mistake :-(. Please try again!")
        print("Suggestion: Try using object-oriented programming to build your solution instead. It may be a little easier to digest. ")
        return jsonify({'error': 'That is not correct. Try again!'}), 500