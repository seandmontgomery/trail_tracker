
from model import connect_to_db, db, User, Trail, TrailMedia
from datetime import datetime

###################### USER ###########################################

def create_user(first_name, email, password):
    """Creates and returns a new user"""

    user = User(first_name=first_name, email=email, password=password)

    db.session.add(user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        user = get_user_by_email(email) 
    return user

###################### TRAIL ###########################################

def create_trail(user_id, trail_name, location, date, difficulty, 
                 terrain, miles, hours, minutes, notes, images, image_urls):
    """Creates and returns trail"""

    trail = Trail(user_id=user_id, location=location, date=date, 
                  difficulty=difficulty, terrain=terrain, miles=miles, hours=hours,
                  minutes=minutes, notes=notes, images=images, image_urls=image_urls)

    db.session.add(trail)
    db.session.commit()

    return trail

###################### TRAIL MEDIA ###########################################

def create_trail_media(trail_id, url, title):
    """Creates and returns trail"""

    trail_media = TrailMedia(trail_id=trail_id, url=url, title=title)
    
    db.session.add(trail_media)
    db.session.commit()

    return(trail_media)
