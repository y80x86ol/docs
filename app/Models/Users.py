from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy.create_engine("mysql://root:root@localhost/blog")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/docs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


def fields():
    return {
        # 用户名
        'username': {
            'type': 'string',
            'default': ''
        },
        # 密码
        'password': {
            'type': 'string',
            'default': ''
        }
    }
