from flask import Flask

from app.Http.Controllers import Home, Test

app = Flask(__name__)


@app.route("/")
def home():
    return Home.index()


@app.route("/test")
def test():
    return Test.index()

@app.route("/test/users")
def test_users():
    return Test.users()

def run():
    app.run()