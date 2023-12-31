from notemanager import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager


class Note(db.Model):
    """Schema for the note model."""
    id = db.Column(db.Integer, primary_key=True)
    note_name = db.Column(db.String(50), nullable=False)
    note_location = db.Column(db.String(50), nullable=False)
    submission_date = db.Column(db.Date, nullable=False)
    note_title = db.Column(db.Text, nullable=False)
    note_message = db.Column(db.Text, nullable=False)
    note_connect = db.Column(db.String(50), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Representation of the Note object."""
        return "#{0} - Name: {1} | Publish: {2}".format(
            self.id, self.note_name, self.publish_date
        )


class User(UserMixin, db.Model):
    """Schema for the user authentication model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        """Representation of the User object."""
        return f"User ID: {self.id}, Username: {self.username}"
