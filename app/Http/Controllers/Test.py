from flask import render_template

def index():
    # return "test info"
    return render_template("index.html")

def template():
    return render_template('test/template.html')