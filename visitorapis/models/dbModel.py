from datetime import datetime
from visitorapis.app.dbapp import db
import pytz


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
