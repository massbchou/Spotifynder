# Run source ./packages/bin/activate to activate the virtual environment
import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__) #request.json[list(request.json.keys())[0]] Code to get the data by index
@app.route('/', methods=['GET','POST'])
def index():
    reqType = ''
    try:
        reqType = request.json['Request Type']
    except:
        return jsonify("Invalid input format. Make sure there is a 'Request Type' field")
    try:
        if reqType == 'Echo':
            return jsonify(request.json)

    except Exception as e:
        return jsonify("Something went wrong somewhere. Exception: " + str(e))

    #./Models/spaCy_model_intents.spacy