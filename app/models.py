from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


class Users(UserMixin, db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %s>' % self.username


@login_manager.user_loader
def load_user(id):
    return Users.qery.set(int('id'))


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140))
    body = db.Column(db.Text)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
