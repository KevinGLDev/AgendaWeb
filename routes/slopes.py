from flask import Blueprint, redirect,render_template, request, url_for
from flask_login import login_required,current_user
from models.slopes import Slopes
from utils.db import db
slopes = Blueprint('slopes',__name__)
import datetime

dateNow = datetime.datetime.now()

@slopes.route('/home/pendientes/registro',methods=['GET','POST'])
@login_required
def registerSlopes():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        dateEnd = request.form['fecha'] +' '+ request.form['hora'] +':00'
        dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
        importance = request.form['importancia']

        slope = Slopes(0,title,content,dateCreation,dateEnd,importance,current_user.id)
        db.session.add(slope)
        db.session.commit()

        return redirect((url_for('users.pendientes')))
    else:
        return render_template('Slopes/registerSlope.html')

@slopes.route('/home/pendientes/update/<id>',methods=['GET','POST'])
@login_required
def update(id):
        slope = Slopes.query.get(id)
        if request.method == 'POST':
            slope = Slopes.query.get(id)
            slope.title = request.form['title']
            slope.content = request.form['content']
            slope.dateEnd = request.form['fecha'] +' '+ request.form['hora'] +':00'
            slope.dateCreation = dateNow.strftime('%Y-%m-%d %H:%M:%S')
            slope.importance = request.form['importancia']
            db.session.commit()

            return redirect((url_for('users.pendientes')))
        else:
            return render_template('Slopes/updateSlope.html',slope = slope)


@slopes.route('/home/pendientes/delete/<id>')
@login_required
def delete(id):

    slope = Slopes.query.get(id)

    db.session.delete(slope)
    db.session.commit()
    return redirect(url_for('users.pendientes'))
        
    


    
