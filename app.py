from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def sample():
    return "Example get api"

@app.route("/coffees", methods=['GET'])
def getCoffes():
    response = requests.get("https://api.sampleapis.com/coffee/hot")
    return jsonify({'info': 'Info from https://sampleapis.com/api-list/coffee, TAGSI group flask demo app', 'data': response.json()})
