import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku


db = SQLAlchemy(app)


# Custom filter function checks if the note publish date is in the past
def past_publish_date(date_string):
    current_date = datetime.now().date()
    publish_date = datetime.strptime(date_string, "%Y/%m/%d").date()
    return publish_date < current_date


# Register the filter function
app.jinja_env.filters['past_publish_date'] = past_publish_date

from notemanager import routes  # noqa
