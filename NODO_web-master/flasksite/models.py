from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flasksite import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#database models
#user
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    firstName=db.Column(db.String(20), nullable=False)
    lastName=db.Column(db.String(20), nullable=False)
    day=db.Column(db.Integer)
    month=db.Column(db.Integer)
    year=db.Column(db.Integer)
    interest1=db.Column(db.String(50))
    interest2=db.Column(db.String(50))
    interest3=db.Column(db.String(50))
    email=db.Column(db.String(120),unique=True, nullable=False)
    password= db.Column(db.String(60),nullable=False)
    status=db.Column(db.String(20),default="pending")
    image_file=db.Column(db.String(20), nullable=False,default="default.jpg")
    #back ref is used to get the user that made the post
    posts=db.relationship('Post',backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.firstName}','{self.lastName}','{self.status}','{self.email}','{self.image_file}')"


    #default expiration time =30 min
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date}')"

