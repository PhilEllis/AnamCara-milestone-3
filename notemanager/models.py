from notemanager import db


class Note(db.Model):
    # schema for the note model
    id = db.Column(db.Integer, primary_key=True)
    note_name = db.Column(db.String(50), nullable=False)
    note_location = db.Column(db.String(50), nullable=False)
    submission_date = db.Column(db.Date, nullable=False)
    note_title = db.Column(db.Text, nullable=False)
    note_message = db.Column(db.Text, nullable=False)
    note_connect = db.Column(db.String(50), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name: {1} | Publish: {2}".format(
            self.id, self.note_name, self.publish_date
        )