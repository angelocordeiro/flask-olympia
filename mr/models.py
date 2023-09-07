from mr.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Mrdata(db.Model, SerializerMixin):
    num = db.Column(db.Integer, primary_key=True)
    vencedor = db.Column(db.String(250))
    peso = db.Column(db.String(250))
    idade = db.Column(db.String(250))
    altura = db.Column(db.String(250))
    ano = db.Column(db.Integer)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
