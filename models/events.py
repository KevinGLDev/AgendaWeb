from utils.db import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    area = db.Column(db.String(100))
    titulo = db.Column(db.String(100))
    content = db.Column(db.String(400))
    dateCreation = db.Column(db.DateTime)
    dateEnd = db.Column(db.DateTime)
    importance = db.Column(db.String(10))
    id_owner = db.Column(db.String(50))


    def __init__(self,id,area,title,content,dateCreation,dateEnd,importance,id_owner):
        self.id = id
        self.area = area
        self.title = title
        self.content = content
        self.dateCreation = dateCreation
        self.dateEnd = dateEnd
        self.importance = importance
        self.id_owner = id_owner


    @classmethod
    def consult(self,area,nivel):
        if nivel == 'Admin':
            list = self.query.all()

            if list != None:
                return list
            else: return None
        else:
            list = self.query.filter(self.area == area)
            if list != None: return list
            else: return None
            

