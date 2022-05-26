from models.users import Users
from models.logins import Logins
from flask import Blueprint, redirect,render_template, request, url_for,flash
from utils.db import db

auth = Blueprint('auth',__name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = Users(request.form['username'],request.form['password'],'','')
        logged_user = Logins.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('auth.home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash('User not found....')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')




@auth.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']

        password_hashed = Users.generate_password(password)

        new_user = Users(username,password_hashed,fullname,email)
        db.session.add(new_user)
        db.session.commit()
        flash("Seccessful Registration")
        return redirect((url_for('auth.login')))
    else:
        return render_template("auth/register.html")

@auth.route('/home')
def home():
    return render_template('users/home.html')