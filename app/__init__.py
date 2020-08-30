from flask import Flask, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from datetime import datetime

from flask_script import Shell, Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import config

bootstrap = Bootstrap()
moment = Moment()
manager = Manager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    return app
