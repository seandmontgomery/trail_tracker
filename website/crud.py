from typing import Optional
from models import db, User

def create_user(first_name: str, email: str, password: str) -> Optional[User]:
    """
    Creates a user, or raises an error if already exists.

    Note: Only 1 user can exist per email address

    Args:
        first_name: first name of this user
        email: email address of this user
        password: non-encrypted password for this user

    Returns: A user object for a new user. If a user with this
       email address already exists, will raise an error
    """
    my_user = User.query.filter_by(email=email).one()
    if my_user:
        raise ValueError('user already exists')

    # otherwise, create a new user
    user = User(first_name=first_name, email=email, password=password)
    db.session.add(user)
    try:
        db.session.commit()
        return user
    except:
        db.session.rollback()
        raise ValueError('could not create a user')