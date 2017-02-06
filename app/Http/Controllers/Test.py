from flask import render_template

from app.Models import Users


def index():
    return render_template("index.html")


def users():
    Users.addUser('admin', 'admin@example.com')
    return '添加用户成功'
