from flask import Blueprint, redirect,render_template, request, url_for
from flask_login import login_required,current_user
from models.slopes import Slopes
from models.notes import Notes
from models.users import Users
from utils.db import db
users = Blueprint('users',__name__)




@users.route('/home',methods=['GET'])
@login_required
def home():


    return render_template('users/home.html')

@users.route('/host/pendientes',methods=['GET'])
@login_required
def pendientes():
    return render_template('users/pendientes.html',list = Slopes.listSlotes(current_user.id))

@users.route('/home/notas',methods=['GET'])
@login_required
def notas():
    return render_template('users/notas.html',list = Notes.listNotes(current_user.id))

@users.route('/home/perfil',methods=['GET','POST'])
@login_required
def perfil():
    if request.method == 'POST':
        user = Users.query.get(current_user.id)
        user.fullname = request.form['fullname']
        user.username = request.form['username']
        password = request.form['password']
        user.email = request.form['email']

        hashPass = Users.generate_password(password)
        user.password = hashPass

    
        db.session.commit()
        return redirect(url_for('users.home'))

    else:
        user = Users.query.get(current_user.id)
        return render_template('users/perfil.html', user = user)

