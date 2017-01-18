from flask import Flask

from app.Http.Controllers import Home,Test

app = Flask(__name__)

@app.route("/")
def home():
    return "hello home"

@app.route("/test")
def test():
    return Test.index()

@app.route("/test/template")
def template():
    return Test.template()

def run():
    app.run()