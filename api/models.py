from main import db
from mongoengine import Document
from mongoengine.fields import(StringField,ListField,ReferenceField, ObjectIdField, BooleanField)
import json, datetime

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String)
#     completed = db.Column(db.Boolean, default=False)
#     due_date = db.Column(db.Date)

 
    

class Todo(Document):
    meta = {'collection': 'todo'}
    # id = ObjectIdField(required=True)
    # id = ObjectIdField(primary_key=True)
    description = StringField(required=True)
    completed= BooleanField()
    due_date = StringField(required=True)


   
    def to_dict(self):
        return {
            # "id": self.pk,
            "id": self.id,
            "completed": self.completed,
            "description": self.description,
            "due_date": self.due_date
        }
