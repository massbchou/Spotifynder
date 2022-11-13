# Run source ./packages/bin/activate to activate the virtual environment
import json
from flask import Flask, request, jsonify
import random
import modelDriver

app = Flask(__name__) #request.json[list(request.json.keys())[0]] Code to get the data by index
@app.route('/', methods=['GET','POST'])
def index():
    reqType = ''
    try:
        reqType = request.json['Request Type']
    except:
        return jsonify("Invalid input format. Make sure there is a 'Request Type' field")
    if reqType is None:
        return jsonify("Invalid input format. Make sure there is a 'Request Type' field")
    try:
        if reqType == 'Echo':
            return jsonify(request.json)
        elif reqType == 'Songify Page':
            mod = request.json['Model']
            if type(mod) is not int:
                return jsonify("Invalid input format. Make sure there is a 'Model' field that is an integer")
            data = request.json['Data']
            if type(data) is not str:
                return jsonify("Invalid input format. Make sure there is a 'Data' field that is a string")

            if (mod == 1):
                return jsonify(modelDriver.predictModel("./models/SAA.spacy", "./models/outputs/output.txt", data)) #Returns an array of the predicted labels.
            else:
                return jsonify("Invalid Model")
    except Exception as e:
        return jsonify("Something went wrong somewhere. Exception: " + str(e))

    #./Models/spaCy_model_intents.spacy

