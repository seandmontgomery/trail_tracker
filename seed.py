import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from website.models import db, User, Trail


#Create a dummy app for seeding the db
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret change for production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://postgres:0821@localhost:5432/trail_tracker')

db.init_app(app)
app.app_context().push()  
#Drop everything
db.drop_all()
#Recreate all tables
db.create_all()

############################## USER #############################################

my_user = User(
    first_name="Sean",
    email="seandmontgomery@gmail.com",
    password=generate_password_hash("password1", method='sha256')
)

# Add to db
db.session.add(my_user)

########################### GRINNELL GLACIER #############################################

my_trail = Trail(
    trail_name="Grinnell Glacier",
    location="Grinnell Glacier, Montana, USA",
    date=datetime(year=2021, month=7, day=26),
    difficulty="advanced",
    terrain="mountain",
    miles=11.1,
    hours=4,
    minutes=13,
    elevation=2087,
    notes="This popular hike, with fabulous views of the Cataract and Grinnell valleys, climbs through pretty meadows and along rock ledges to Upper Grinnell Lake and Grinnell Glacier, cradled in a dramatic cirque along the Continental Divide. A dramatic cirque of rugged peaks and jagged ridges, anchored by Mt. Grinnell (8,851-ft.) to the north and Mt. Gould (9,553-ft.) to the south, towers above the head of the Grinnell Valley. Three glaciers, the Grinnell, Salamander and Gem, along with Upper Grinnell Lake lie nestled beneath this imposing wall of rock. The popular hike to Grinnell Glacier climbs the northwestern flanks of Mt. Grinnell to a high bench beneath this stunning cirque, offering fabulous views of the glaciers and Upper Grinnell Lake. Along the way the trail travels through pretty meadows sprinkled with wildflowers, traverses narrow ledges and enjoys panoramic views of the Cataract and Grinnell valleys. Beautiful Grinnell Falls, fed by glacial melt water, spills down the valley’s headwall to Grinnell Lake, cradled on the valley floor. Good opportunities exist for spotting mountain goats and big horn sheep on the cliffs overhead as well as the meadows below the trail. Do not expect solitude on the trail. This is an extremely popular hike. During the height of the season large numbers of hikers take the daily ranger led tours visiting the glacier.",
)

my_user.trail.append(my_trail)

my_media = [
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309858/szjmwhddbhtyvn79pxgb.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309859/nks6cyjny5cesgr7yfjo.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309861/tysm7jyyrxeohkywloyw.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309862/nmwso5jsngqmdjwurolx.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309863/wvw1zhffy4xmsuhphpeh.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309865/jklbxolrd5xlcqzcxxrb.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309866/psna9uvobhjsolxvnigz.jpg'

]

my_trail.image_urls = [{'url': x} for x in my_media]

########################### GRINNELL #############################################

my_trail = Trail(
    trail_name="Grinnell Glacier",
    location="Grinnell Glacier, Montana, USA",
    date=datetime(year=2021, month=7, day=26),
    difficulty="advanced",
    terrain="mountain",
    miles=11.1,
    hours=4,
    minutes=3,
    elevation=2087,
    notes="This popular hike, with fabulous views of the Cataract and Grinnell valleys, climbs through pretty meadows and along rock ledges to Upper Grinnell Lake and Grinnell Glacier, cradled in a dramatic cirque along the Continental Divide. A dramatic cirque of rugged peaks and jagged ridges, anchored by Mt. Grinnell (8,851-ft.) to the north and Mt. Gould (9,553-ft.) to the south, towers above the head of the Grinnell Valley. Three glaciers, the Grinnell, Salamander and Gem, along with Upper Grinnell Lake lie nestled beneath this imposing wall of rock. The popular hike to Grinnell Glacier climbs the northwestern flanks of Mt. Grinnell to a high bench beneath this stunning cirque, offering fabulous views of the glaciers and Upper Grinnell Lake. Along the way the trail travels through pretty meadows sprinkled with wildflowers, traverses narrow ledges and enjoys panoramic views of the Cataract and Grinnell valleys. Beautiful Grinnell Falls, fed by glacial melt water, spills down the valley’s headwall to Grinnell Lake, cradled on the valley floor. Good opportunities exist for spotting mountain goats and big horn sheep on the cliffs overhead as well as the meadows below the trail. Do not expect solitude on the trail. This is an extremely popular hike. During the height of the season large numbers of hikers take the daily ranger led tours visiting the glacier.",
)

my_user.trail.append(my_trail)

my_media = [
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309858/szjmwhddbhtyvn79pxgb.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309859/nks6cyjny5cesgr7yfjo.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309861/tysm7jyyrxeohkywloyw.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309862/nmwso5jsngqmdjwurolx.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309863/wvw1zhffy4xmsuhphpeh.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309865/jklbxolrd5xlcqzcxxrb.jpg',
    'https://res.cloudinary.com/seandmontgomery/image/upload/v1647309866/psna9uvobhjsolxvnigz.jpg'

]

my_trail.image_urls = [{'url': x} for x in my_media]


# Next trail goes here

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

try:
    db.session.commit()
except:
    db.session.rollback()