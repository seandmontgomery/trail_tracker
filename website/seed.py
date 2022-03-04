import os
import json
from datetime import datetime
import crud
import model
import server
from utils.cipher import hashed 

os.system('dropdb trail_tracker')
os.system('createdb trail_tracker')

model.connect_to_db(server.app)
model.db.create_all()

##############################USER#############################################

sm = crud.create_user(first_name="Sean",
                      email="seandmontgomery@gmail.com",
                      password=hashed("password1"),
                      )

###########################TRAIL#############################################

grinnell = crud.create_trail(user_id=1, 
                            trail_name="Grinnell Glacier", 
                            location="Grinnell Glacier, Montana, USA", 
                            date="2020-02-01", 
                            difficulty="advanced", 
                            terrain="mountain", 
                            miles="12", 
                            hours="7", 
                            minutes="30", 
                            notes="This was a beautiful hike!!",
                            )

###########################TRAIL MEDIA#############################################

grinnell_media = crud.create_trail_media(trail_id=1,
                            url="http://res.cloudinary.com/seandmontgomery/image/upload/v1646146829/l7dyoilmofxvg0austxm.jpg",
                            title="placeholder"
                            )

grinnell_media = crud.create_trail_media(trail_id=1,
                            url="http://res.cloudinary.com/seandmontgomery/image/upload/v1646146831/q9zeyx0cjhkzrp20hp93.jpg",
                            title="placeholder"
                            )