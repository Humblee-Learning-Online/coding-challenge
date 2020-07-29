from .import bp as main
from flask import jsonify, request
import requests
from app.data import data

@main.route('/', methods=['GET'])
def index():
    return jsonify(data)