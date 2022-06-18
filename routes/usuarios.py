from multiprocessing import Event
from flask import Blueprint, redirect,render_template, request, url_for
from flask_login import login_required,current_user
from models.slopes import Slopes
from models.notes import Notes
from models.users import Users
from models.events import Events
from utils.db import db
import datetime

dateNow = datetime.datetime.now()

users = Blueprint('users',__name__)




@users.route('/home',methods=['GET'])
@login_required
def home():
    if current_user.nivel == 'Admin': return render_template('users/homeA.html')
    elif current_user.nivel == 'Gestor': return render_template('users/homeG.html')
    elif current_user.nivel == 'Colaborador': return render_template('users/homeC.html')

    

@users.route('/host/pendientes',methods=['GET'])
@login_required
def pendientes():
    list = Slopes.listSlotes(current_user.id)
    if list != None:
        return render_template('users/pendientes.html',list = Slopes.listSlotes(current_user.id))
    else:
        return render_template('users/pendientesVacios.html')


@users.route('/home/notas',methods=['GET'])
@login_required
def notas():
    list  = Notes.listNotes(current_user.id)
    if list != None:
            list  = Notes.listNotes(current_user.id)
            return render_template('users/notas.html',list = list )
    else:        
        return render_template('users/notasVacias.html')

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

@users.route('/home/eventos',methods=['GET'])
@login_required
def eventos():
    list = Events.consult(current_user.area,current_user.nivel)
    

    return render_template('users/eventos.html', list = list)

@users.route('/home/eventos/register',methods=['GET','POST'])
@login_required
def eventosRegister():
    if request.method == 'POST':
        if current_user.nivel == 'Admin':
            title = request.form['title']
            content = request.form['content']
            dateEnd = request.form['fecha'] +' '+ request.form['hora'] +':00'
            dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
            importance = request.form['importancia']
            area = request.form['area']
            event = Events(0,area,title,content,dateCreation,dateEnd,importance,current_user.fullname)
            db.session.add(event)
            db.session.commit()
            return redirect((url_for('users.eventos')))
        else:
            title = request.form['title']
            content = request.form['content']
            dateEnd = request.form['fecha'] +' '+ request.form['hora'] +':00'
            dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
            importance = request.form['importancia']
            area = current_user.area
            event = Events(0,area,title,content,dateCreation,dateEnd,importance,current_user.fullname)
            db.session.add(event)
            db.session.commit()
            return redirect((url_for('users.eventos')))
            
        
    else:
        return render_template('events/registerEvents.html')

@users.route('/home/eventos/delete/<id>',methods=['GET','POST'])
@login_required
def eliminarEvento(id):
    event = Events.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('users.eventos'))

@users.route('/home/eventos/update/<id>',methods=['GET','POST'])
@login_required
def modificarEvento(id):
    event = Events.query.get(id)
    if request.method == 'POST':
        event.title = request.form['title']
        event.content = request.form['content']
        event.dateEnd = request.form['fecha'] +' '+ request.form['hora'] +':00'
        event.dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
        event.importance = request.form['importancia']
        event.id_owner = current_user.fullname
        
        db.session.commit()
        return redirect((url_for('users.eventos')))
    else:
        return render_template('events/updateEvents.html', event = event)

