from app.Models import BaseModel

db = BaseModel.connect()


# 模型
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


# 添加一个用户
def addUser(username, email):
    user = Users(username, email)
    db.session.add(user)
    db.session.commit()
    return 1


def deleteUser(uid):
    user = Users.query.filter(Users.id == '3').first()
    db.session.delete(user)
    db.session.commit()
    return 1


def userList():
    userList = Users.query.all()
    return userList
