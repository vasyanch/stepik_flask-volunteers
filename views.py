from flask import request, jsonify

from volunteers.app import app
from volunteers.models import Volunteer, District, Street, Request


@app.route('/districts/', methods=['GET'])
def get_districts():
    pass


@app.route('/streets/', methods=['GET'])
def get_streets():
    pass


@app.route('/volunteers/', methods=['GET'])
def get_volunteers():
    street = request.args.get('street')
    volunteers = Volunteer.query
    if street:
        volunteers = volunteers.join(Volunteer.streets).filter(Street.id == street)

    return [volunteer.serialize for volunteer in volunteers], 200


@app.route('/helpme/', methods=['POST'])
def get_help():
    return jsonify, 201
