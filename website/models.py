from . import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    trail = db.relationship('Trail')

class Trail(db.Model):

    __tablename__ = 'trail'

    id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.Date)
    difficulty = db.Column(db.String)
    trail_type = db.Column(db.String)
    miles = db.Column(db.Integer)
    hours = db.Column(db.Integer)
    minutes = db.Column(db.Integer)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    image_url = db.Column(db.String)

    def add_image(self, image_blob):
        """Add an image to a trail object"""

        # do upload to cloudinary
        pass

        # do get url
        pass

        # do add to images table
        pass

        # associate with object
        pass
