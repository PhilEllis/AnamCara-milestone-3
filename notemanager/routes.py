from flask import render_template, request, redirect, url_for, flash
from notemanager import app, db, login_manager
from notemanager.models import (
    Note,
    User,
    generate_password_hash,
    check_password_hash,
)
from flask_login import (
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired, Email
from flask_wtf import FlaskForm


@login_manager.user_loader
def load_user(user_id):
    """Callback to reload user object from user ID."""
    return User.query.get(user_id)


class LoginForm(FlaskForm):
    """Form for user login."""
    username = StringField(
        'username', validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        'password', validators=[InputRequired(), Length(min=8, max=80)]
    )
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    """Form for user registration."""
    username = StringField(
        'username', validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        'password', validators=[InputRequired(), Length(min=8, max=80)]
    )


@app.route("/")
def home():
    """Render the home page."""
    return render_template("home.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash('You have successfully logged in!', 'success')
                return redirect(url_for('notes'))
            else:
                flash('Invalid username or password', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle user registration."""
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256'
        )
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash(('Welcome, {}! You have successfully signed up. '
               'Please login.').format(new_user.username), 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('home'))


@app.route("/notes")
def notes():
    """Render the notes page."""
    notes = Note.query.order_by(Note.id.desc()).all()
    return render_template("notes.html", notes=notes)


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    """Handle adding a new note."""
    if request.method == "POST":
        note = Note(
            note_name=request.form.get("note_name"),
            note_location=request.form.get("note_location"),
            submission_date=request.form.get("submission_date"),
            note_title=request.form.get("note_title"),
            note_message=request.form.get("note_message"),
            note_connect=request.form.get("note_connect"),
            publish_date=request.form.get("publish_date"),
            user_id=current_user.id
        )
        db.session.add(note)
        db.session.commit()

        flash(("Whisper submitted! Messages published at 00:00 GMT the day"
               " after the selected publish date"), "success")

        return redirect(url_for("notes"))
    return render_template("add_note.html")


@app.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    """Handle editing a note."""
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


@app.route("/delete_note/<int:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    """Handle deleting a note."""
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes"))
