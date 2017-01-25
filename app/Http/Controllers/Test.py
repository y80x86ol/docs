from flask import render_template

from app.Models import Users


def index():
    return render_template("index.html")


def users():
    admin = Users('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return '234'
