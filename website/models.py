"""
ORM to manage relationship between backend service and Postgres DB

References:
    1. https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#declarative-table-configuration
    2. https://docs.sqlalchemy.org/en/14/orm/extensions/associationproxy.html
"""
import datetime

from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from . import db

######################USER###################################

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    trail = db.relationship('Trail')

    def get_trail_attribute_counts(self, attribute: str) -> dict:
        """
        Returns the frequency (count) of trail attributes as a dictionary,
        suitable for plotting with chart.js

        Args:
            attribute: an attribute of the trail you want to enumerate

        Ex:
            >> user.get_trail_attribute_counts('terrain')
            {'mountain': 1, 'forest': 2}
        """

        #Make sure the trail has the attribute

        if not hasattr(Trail, attribute):
            raise ValueError('must submit a valid Trail attribute')

        my_dict = {}

        for trail in self.trail:
            key = getattr(trail, attribute)
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1

        return my_dict

######################TRAIL################################### 

class Trail(db.Model):
    """
    To access images for a specific trail - you can 
    do it in the following ways:

        1. Just get the URL attribute for each image, 
            as an array of URLS.

            >> trail.image_urls
            ['url_1', 'url_2']
        
        2. Create an array of dictionaries of 
            spcified attributes for each image

            >> [{'title': x.title, 'url': x.url} for x in trail.images]
            [
                {'title': 'title_1', 'url': 'url_1'}, 
                {'title': 'title_2', 'url': 'url_2'}
            ]
    """
    __tablename__ = 'trail'

    id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.Date)
    difficulty = db.Column(db.String)
    terrain = db.Column(db.String)
    miles = db.Column(db.Integer)
    hours = db.Column(db.Integer)
    minutes = db.Column(db.Integer)
    elevation = db.Column(db.Integer)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    images = db.relationship('TrailMedia')

    # Association proxies explained in [2]
    image_urls = association_proxy('images', 'url',
        creator=lambda kwargs: TrailMedia(**kwargs)
    )

    @hybrid_property
    def cover_image(self):
        """
        Returns cover image as a calculated attribute
        """
        return next(iter(self.image_urls), None)

######################TRAIL MEDIA################################### 

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
    title = db.Column(db.String, comment='media title')

    def get_photos_by_trail(trail_id):
    
        photos = TrailMedia.query.filter(TrailMedia.trail_id == trail_id).all()

        return photos