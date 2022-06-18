
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flasksite.config import Config


#run from terminal and set EMAIL_USER and EMAIL_PASS in the terminal using nano .bash_profile for mac
# app = Flask(__name__)
# app.config.from_object(Config)
db = SQLAlchemy()
bcrypt= Bcrypt()
login_manager =LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from flasksite.users.routes import users
    from flasksite.posts.routes import posts
    from flasksite.main.routes import main
    from flasksite.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)


    return app
