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
    # print(request.json.get('data'))
    # print(request.get('data'))
    # print(request.get('json'))
    # print(request.get('json')
    try:
        # if json.dumps(conference_data) == request.json['data']:
        if conference_data == list(request.json.values())[0]:
            print('Success')
            return jsonify({'message': 'Success'}), 200
    except Exception as error:
        print()
        print("="*120)
        print("Oops! Somewhere along the way, you made a mistake :-(. Please try again!")
        print("Suggestion: Try using object-oriented programming to build your solution instead. It may be a little easier to digest. ")
        print("="*120)

        print()
        print("="*120)
        print(error)
        print("="*120)
        print()
        return jsonify({'error': f'{error}'}), 400