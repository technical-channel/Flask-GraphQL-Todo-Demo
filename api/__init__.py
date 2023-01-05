import os

from ariadne import QueryType
from flask import Flask
#from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
#from mongoengine.fields import (DateTimeField, ReferenceField, StringField)
from mongoengine import Document
from mongoengine.fields import StringField

# import pymongo
# from pymongo import MongoClient
import bson
import json
from jsonpath import jsonpath
from mongoengine import connect
import os


try:
    db = "TODOAPP"
    PASSWORD = "rahul"

    client = connect(
        db,
        host=f"mongodb+srv://rahul:{PASSWORD}@cluster0.aojqm.mongodb.net/?retryWrites=true&w=majority",
        alias="default",
    )
    print("connection successful")
except:
    print("not connecting")
#client.drop_database(DATABASE)


#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


query = QueryType()


@app.route('/')
def hello():
    return """<p>Click on this button : </p>
    <button class="graphql" 
    onclick="window.location.href = 'http://127.0.0.1:5000/graphql';">
        graphql
    </button>"""


if __name__ == '__main__':
    app.run(debug=True)
