from flask import Blueprint,render_template
from flask_login import login_required,current_user
users = Blueprint('users',__name__)




@users.route('/home',methods=['GET'])
@login_required
def home():
    return render_template('users/home.html')

@users.route('/host/pendientes',methods=['GET'])
@login_required
def pendientes():
    return render_template('users/pendientes.html')

@users.route('/home/notas',methods=['GET'])
@login_required
def notas():
    return render_template('users/notas.html')

@users.route('/home/perfil',methods=['GET'])
@login_required
def perfil():
    return render_template('users/perfil.html')

