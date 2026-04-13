from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster      = db.Column(db.String(255), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)