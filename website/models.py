from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    trail = db.relationship('Trail')

class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String)
    date = db.Column(db.Date)
    location = db.Column(db.String)
    mileage = db.Column(db.Integer)
    time = db.Column(db.Integer)
    notes = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, server_default='This is a value')


