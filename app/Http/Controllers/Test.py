from flask import render_template

from app.Models import Users


def index():
    return render_template("test/template.html")


def addUser():
    addResult = Users.addUser('admin', 'admin@example.com')
    return '添加用户成功'


def userList():
    userList = Users.userList()
    return render_template("user/list.html", userList = userList)


def deleteUser(uid):
    deleteResult = Users.delete(uid)
    return '删除成功'
