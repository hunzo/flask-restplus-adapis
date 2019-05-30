from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/mydb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class BindUserTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    domain = db.Column(db.String(50))
    basedn = db.Column(db.String(50))
    bindou = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.now(
        pytz.timezone("Asia/Bangkok")))
    serverip = db.Column(db.String(20))
