from turtle import title
from utils.db import db

class Notes(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(500))
    dateCreation = db.Column(db.DateTime) 
    id_owner = db.Column(db.Integer)
    

    def __init__(self,id,title,content,dateCreation,id_owner):
        self.id = id          
        self.title = title
        self.content = content
        self.dateCreation = dateCreation
        self.id_owner = id_owner

    @classmethod
    def listNotes(self,id_owner):

        list = self.query.filter(self.id_owner == id_owner)

        if list.first() !=None:
            
            return list

        else:
            print("============================")
            print('NO RETORNO NADA')
            print("============================")
            return None


        