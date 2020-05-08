from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


street_district_association = db.Table(
    'district_street_association', db.metadata,
    db.Column('District', db.Integer, db.ForeignKey('districts.id'), nullable=False),
    db.Column('Street', db.Integer, db.ForeignKey('streets.id'), nullable=False)
)


class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    streets = db.relationship('Street', secondary=street_district_association, back_populates='districts')


street_volunteer_association = db.Table(
    'street_volunteer_association', db.metadata,
    db.Column('Street', db.Integer, db.ForeignKey('streets.id'), nullable=False),
    db.Column('Volunteer', db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
)


class Street(db.Model):
    __tablename__ = 'streets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    districts = db.relationship('District', secondary=street_district_association, back_populates='streets')
    volunteers = db.relationship('Volunteer', secondary=street_volunteer_association, back_populates='streets')
    requests = db.relationship('Request', back_populates='street')


class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    userpic = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    streets = db.relationship('Street', secondary=street_volunteer_association, back_populates='volunteers')
    requests = db.relationship('Request', back_populates='volunteer')


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'))
    volunteer = db.relationship('Volunteer', back_populates='requests')
    street_id = db.Column(db.Integer, db.ForeignKey('streets.id'), nullable=False)
    street = db.relationship('Street', back_populates='requests')
    address = db.Column(db.String, nullable=False)
    client_name = db.Column(db.String, nullable=False)
    client_surname = db.Column(db.String)
    client_phone = db.Column(db.String)
    text = db.Column(db.Text)
