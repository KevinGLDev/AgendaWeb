from werkzeug.security import check_password_hash,generate_password_hash
from utils.db import db
from flask_login import UserMixin


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(110)) 
    username = db.Column(db.String(100))

    def __init__(self,id,username,password,fullname,email):
        self.id = id
        self.username= username
        self.fullname = fullname
        self.email = email
        self.password = password
        

    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)

    @classmethod
    def generate_password(self,password):
        return generate_password_hash(password)

