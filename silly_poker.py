from flask import Flask, render_template, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import utils

# remeber to export FLASK_APP="silly_poker.py"

conf = utils.conf
app = Flask(__name__)
app.config.update(conf)
db = SQLAlchemy(app)
Session(app)

#This must be imported after db is initialized cause models depends on it
import models
import forms

@app.route("/")
def hello_world():
    form = forms.LoginForm()
    return render_template("login.html", form=form)

@app.route("/set/")
def set():
    session["key"]="set"
    return "ok"

@app.route("/unset/")
def unset():
    del session["key"]
    return "ok"

@app.route("/get/")
def get():
  return session.get("key","unset")
