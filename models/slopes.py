# from turtle import title
# from utils.db import db

# class slopes(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(400))
#     dateCreation = db.Column(db.String(50)) ##METER FECHAS A UNA BASE DE DATOS
#     dateEnd = db.Column(db.String(50))
#     importance = db.Column(db.Integer)
#     id_owner = db.Column(db.Integer)

#     def __init__(self,title,content,dateCreation,dateEnd,importance,id_owner):
        
#         self.title = title
#         self.content = content
#         self.dateCreation = dateCreation
#         self.dateEnd = dateEnd
#         self.importance = importance
#         self.id_owner = id_owner