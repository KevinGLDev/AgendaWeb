from flask import Flask
from routes.auth import auth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/agenda_web'
app.config['SQLALCHEMY_TRACK_modifications'] = False
app.config['SECRET_KEY'] = 'B!1weNAt1T^%kvhUI*S^'

SQLAlchemy(app)

app.register_blueprint(auth)



