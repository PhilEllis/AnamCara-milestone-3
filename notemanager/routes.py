from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        note = Note(
            note_name=request.form.get("note_name"),
            note_location=request.form.get("note_location"),
            submission_date=request.form.get("submission_date"),
            note_title=request.form.get("note_title"),
            note_message=request.form.get("note_message"),
            note_connect=request.form.get("note_connect"),
            publish_date=request.form.get("publish_date")
        )
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("notes"))
    return render_template("add_note.html")
