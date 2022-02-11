from . import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    trail = db.relationship('Trail')
    media = db.relationship('Media')

class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.Date)
    miles = db.Column(db.Integer)
    hours = db.Column(db.Integer)
    minutes = db.Column(db.Integer)
    notes = db.Column(db.String)
    image_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_title = db.Column(db.String)
    media_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))