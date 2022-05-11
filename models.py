from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    address = db.Column(db.String(1000))
    phone = db.Column(db.String(1000))
    grade = db.Column(db.String(1000))
    age = db.Column(db.String(1000))
    team = db.Column(db.String(1000))
    car = db.Column(db.String(1000)) 
    officer = db.Column(db.Boolean)