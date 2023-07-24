import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_migrate import Migrate

if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

bootstrap = Bootstrap(app)

"""Create an instance of LoginManager"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

"""Configure the database"""
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)


migrate = Migrate(app, db)


def past_publish_date(date_string):
    """Custom filter function that checks note publish date is in the past."""
    current_date = datetime.now().date()
    date_string = date_string.strftime("%Y/%m/%d")
    publish_date = datetime.strptime(date_string, "%Y/%m/%d").date()
    return publish_date < current_date


"""Register the filter function"""
app.jinja_env.filters['past_publish_date'] = past_publish_date


from notemanager import routes  # noqa
