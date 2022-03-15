from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db= SQLAlchemy()


class Todo(db.Model):
    sno=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(200))
    disc=db.Column(db.String(300))
    date_created=db.Column(db.Datetime,default=datetime.utcnow)