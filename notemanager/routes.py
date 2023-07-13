from flask import render_template
from notemanager import app, db
from notemanager.models import Note


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/add_note", methods=["GET", "POST"])
def add_note():
    return render_template("add_note.html")