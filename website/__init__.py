from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "trail_tracker.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret change for production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:0821@localhost:5433/trail_tracker')
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import your models - connect classes to database
    from .models import User, Trail
    # this create opperation creates all tables in my target db
    # this is different from a migration
    # todo: read up on db migrations
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')