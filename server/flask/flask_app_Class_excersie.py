#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pandas as pd
import random

app = Flask(__name__)

persons = []
firstnames = ['Pelle','Bo','Niklas','Ulla', 'Stine', 'Lars']
lastnames = ['Pedersen', 'Dahl', 'Christiansen', 'Petersen', 'Hansen', 'Strøm']

for i in range(1,100+1):
    tmp_person = {
        'id': i,
        'navn': random.choice(firstnames) + " " + random.choice(lastnames)
    }
    persons.append(tmp_person)

@app.route('/')
def hello_world():
    return 'Persons project'

@app.route('/datagen/api/person/<int:no>', methods=['GET'])
def get_persons_to_100(no):
    return jsonify(persons[:no])



@app.route('/datagen/api/person', methods=['POST'])
def add_person():
    if not request.json or not 'navn' in request.json:
        abort(400)
    new_person = {
        'id': persons[-1]['id'] + 1,
        'navn': request.json['navn'],
    }
    persons.append(new_person)
    return jsonify(new_person)
