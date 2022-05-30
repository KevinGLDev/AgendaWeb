from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



login_mannager_app = LoginManager()
login_mannager_app.login_view = 'auth.login'
login_mannager_app.login_message_category = 'info'

def create_app():

        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/agenda_web'
        app.config['SQLALCHEMY_TRACK_modifications'] = False
        app.config['SECRET_KEY'] = 'B!1weNAt1T^%kvhUI*S^'
        login_mannager_app.init_app(app)
        SQLAlchemy(app)


        from routes.auth import auth
        from routes.usuarios import users
        app.register_blueprint(auth)
        app.register_blueprint(users)

        return app



  