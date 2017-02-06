from flask import Flask

from app.Http.Controllers import Home, Test

app = Flask(__name__)


@app.route("/")
def home():
    return Home.index()


@app.route("/test")
def test():
    return Test.index()


@app.route("/test/user/add")
def test_add_user():
    return Test.addUser()


@app.route("/test/user/delete")
def test_user_delete():
    return Test.deleteUser()


@app.route("/test/user")
def test_user():
    return Test.userList()


def run():
    app.run()
