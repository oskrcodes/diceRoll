from flask import Flask

app = Flask(__name__)


@app.route("/") 
def hello():
    return "<h1>home page!</h1>"


@app.route("/about")
def about():
    return "<p>about info</p>"