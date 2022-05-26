from flask import Blueprint,render_template

users = Blueprint('users',__name__)

@users.route('/')
def home():
    return render_template('home.html')

@users.route('/Pendientes')
def pendientes():
    return render_template('pendientes.html')

@users.route('/Notas')
def notas():
    return render_template('notas.html')

@users.route('/Perfil')
def perfil():
    return render_template('perfil.html')
