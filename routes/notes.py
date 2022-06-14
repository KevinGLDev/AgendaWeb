from flask import Blueprint,render_template, request,redirect,url_for
from flask_login import login_required,current_user
from models.notes import Notes
from utils.db import db
notes = Blueprint('notes',__name__)
import datetime

dateNow = datetime.datetime.now()

@notes.route('/home/notas/registro',methods=['GET','POST'])
@login_required
def registerNotes():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        dateCretion = dateNow.strftime('%Y-%m-%d %H:%M:%S')
        importance = request.form['importancia']
        
        note = Notes(0,title,content,dateCretion,current_user.id)
        db.session.add(note)
        db.session.commit()

        return redirect((url_for('users.notas')))
    else:
        return render_template('notes/registerNotes.html')

@notes.route('/home/notas/update/<id>',methods=['GET','POST'])
@login_required
def update(id):
    note = Notes.query.get(id)
    if request.method == 'POST':
        note = Notes.query.get(id)
        note.title = request.form['title']
        note.content = request.form['content']
        note.dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
        note.importance = request.form['importancia']

        db.session.commit()

        return redirect((url_for('users.notas')))

    return render_template('notes/updateNotes.html', note = note)


@notes.route('/home/notes/delete/<id>',methods=['GET','POST'])
@login_required
def delete(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('users.notas'))