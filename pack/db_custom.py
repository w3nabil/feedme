from . import db 
from flask_login.mixins import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(25))
    name = db.Column(db.String(20))
    fa2 = db.Column(db.String(50))
    profile_pic = db.Column(db.String(200), default='img/default-profile.png')
    cover_pic = db.Column(db.String(100), default='img/default-cover.jpg')
    hometown = db.Column(db.String(50))
    bio = db.Column(db.String(300)) 
    date = db.Column(db.String(20), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class FormQue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shorturl = db.Column(db.String(8), unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    question1 = db.Column(db.String(300))
    question2 = db.Column(db.String(300))
    question3 = db.Column(db.String(300))
    question4 = db.Column(db.String(300))
    question5 = db.Column(db.String(300))
    question6 = db.Column(db.String(300))
    question7 = db.Column(db.String(300))
    question8 = db.Column(db.String(300))
    question9 = db.Column(db.String(300))
    question10 = db.Column(db.String(300))
    user = db.Column(db.String(32))
    date = db.Column(db.String(20), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class FormAns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(32))
    name = db.Column(db.String(20))
    email = db.Column(db.String(30))
    answer1 = db.Column(db.String(300))
    answer2 = db.Column(db.String(300))
    answer3 = db.Column(db.String(300))
    answer4 = db.Column(db.String(300))
    answer5 = db.Column(db.String(300))
    answer6 = db.Column(db.String(300))
    answer7 = db.Column(db.String(300))
    answer8 = db.Column(db.String(300))
    answer9 = db.Column(db.String(300))
    answer10 = db.Column(db.String(300))
    date = db.Column(db.String(20), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    shorturl = db.Column(db.String(8))
