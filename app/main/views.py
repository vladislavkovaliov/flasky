from . import main
from datetime import datetime
from flask import render_template, session, url_for, redirect
from .forms import NameForm
from ..models import User
from .. import db
from flask import current_app
from ..emails import send_email


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
