"""
ORM to manage relationship between backend service and Postgres DB

References:
    1. https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#declarative-table-configuration
    2. https://docs.sqlalchemy.org/en/14/orm/extensions/associationproxy.html
"""
import datetime

from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy

from . import db


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

    images = db.relationship('TrailMedia')

    # Association proxies explained in [2]
    image_urls = association_proxy('images', 'url',
        creator=lambda url: TrailMedia(url=url)
    )


class TrailMedia(db.Model):

    __tablename__ = 'trail_media'
    __table_args__ = {
        'comment': 'trail related media – url and associated metadata. '
            '(Media binary is stored in cloudinary)'
    }

    id = db.Column(db.Integer, primary_key=True)
    trail_id = db.Column(db.Integer, db.ForeignKey('trail.id'),
        comment='All media in this table is associated with a given trail'
    )
    url = db.Column(db.String, comment='cloudinary url (publically accessible link)')
