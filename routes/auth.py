
from models.users import Users
from models.logins import Logins
from flask import Blueprint, redirect,render_template, request, url_for,flash
from utils.db import db
from flask_login import login_user, logout_user,login_required
from app import login_mannager_app

@login_mannager_app.user_loader
def get_id(id):
    return Logins.get_id(id)


auth = Blueprint('auth',__name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = Users(0,request.form['username'],request.form['password'],'','')
        logged_user = Logins.login(user)
        if logged_user != None:
            if logged_user.password:

                login_user(logged_user)
                return redirect(url_for('users.home'))
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

        new_user = Users(0,username,password_hashed,fullname,email)
        db.session.add(new_user)
        db.session.commit()
        flash("Seccessful Registration")
        return redirect((url_for('auth.login')))
    else:
        return render_template("auth/register.html")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


