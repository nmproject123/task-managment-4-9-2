from flask import Blueprint, jsonify, request
from BL.persons_bl import PersonBL
persons = Blueprint('persons', __name__)

person_bl = PersonBL()

# Get All
# localhost:port/persons
@persons.route("/", methods=['GET'])
def get_all_persons():
    persons = person_bl.get_all_persons()
    return jsonify(persons)
# get one
@persons.route("/<id>/", methods=['GET'])
def get_person(id):
    person = person_bl.get_person(id)
    return jsonify(person)

# ADD person
@persons.route("/", methods=['POST'])
def add_person():
    per = request.json
    status = person_bl.add_person(per)
    return jsonify(status)

#Update Person

@persons.route("/<id>/", methods=['PUT'])
def update_person(id):
    obj = request.json
    print(obj)
    print(id)
    result = person_bl.update_person(id,obj)
    return jsonify(result)


#Delete
@persons.route("/<id>/", methods=['DELETE'])
def dlelete_person(id):
    result = person_bl.delete_person(id)
    return jsonify(result)
