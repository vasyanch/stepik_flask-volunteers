from flask import request, jsonify

from volunteers.app import app
from volunteers.models import db, Volunteer, District, Street, Request


@app.route('/districts/', methods=['GET'])
def get_districts():
    districts = District.query.order_by(District.title)
    return jsonify([district.serialize for district in districts]), 200


@app.route('/streets/', methods=['GET'])
def get_streets():
    district_id = request.args.get('district')
    streets = db.session.query(Street)
    if district_id:
        streets = streets.join(Street.districts).filter(District.id == int(district_id))
    return jsonify([street.serialize for street in streets]), 200


@app.route('/volunteers/', methods=['GET'])
def get_volunteers():
    street = request.args.get('street')
    volunteers = db.session.query(Volunteer)
    if street:
        volunteers = volunteers.join(Volunteer.streets).filter(Street.id == street)
    return jsonify([volunteer.serialize for volunteer in volunteers.order_by(Volunteer.name)]), 200


@app.route('/help_requests/<int:request_id>/', methods=['GET'])
def get_help_request(request_id):
    help_request = Request.query.get(request_id)
    if help_request:
        return jsonify(help_request.serialize), 200
    return jsonify(), 404


@app.route('/helpme/', methods=['POST'])
def post_help():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'failed'}), 400
    try:
        help_request = Request(
            district_id=data['district'],
            street_id=data['street'],
            volunteer_id=data['volunteer'],
            address=data['address'],
            client_name=data['name'],
            client_surname=data['name'],
            client_phone=data['phone'],
            text=data['text']
        )
    except KeyError:
        return jsonify({'status': 'failed'}), 400
    db.session.add(help_request)
    db.session.commit()
    return jsonify({'status': 'success', 'request_id': help_request.id}), 201, \
           {"Location": f"/help_requests/{help_request.id}/"}
