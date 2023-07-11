from flask import render_template
from notemanager import app, db
from notemanager.models import Note


@app.route("/")
def home():
    return render_template("base.html")