from flask import render_template, request, redirect, url_for
from notemanager import app, db
from notemanager.models import Note, User
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/notes")
def notes():
    notes = Note.query.order_by(Note.id.desc()).all()  # Retrieve all notes
    return render_template("notes.html", notes=notes)


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


@app.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.note_name = request.form.get("note_name")
        note.note_location = request.form.get("note_location")
        note.submission_date = request.form.get("submission_date")
        note.note_title = request.form.get("note_title")
        note.note_message = request.form.get("note_message")
        note.note_connect = request.form.get("note_connect")
        note.publish_date = request.form.get("publish_date")
        db.session.commit()
        return redirect(url_for("notes"))
    return render_template("edit_note.html", note=note)


@app.route("/delete_note/<int:note_id>")
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes"))
