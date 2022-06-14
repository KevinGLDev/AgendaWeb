from turtle import title
from utils.db import db

class Slopes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(400))
    dateCreation = db.Column(db.DateTime)
    dateEnd = db.Column(db.DateTime)
    importance = db.Column(db.String(10))
    id_owner = db.Column(db.Integer)

    def __init__(self,id,title,content,dateCreation,dateEnd,importance,id_owner):
        self.id = id
        self.title = title
        self.content = content
        self.dateCreation = dateCreation
        self.dateEnd = dateEnd
        self.importance = importance
        self.id_owner = id_owner

    @classmethod
    def listSlotes(self,id_owner):

        list = self.query.filter(self.id_owner == id_owner)

        if list.first() !=None:
            
            return list

        else:
            print("============================")
            print('NO RETORNO NADA')
            print("============================")
            return None

    