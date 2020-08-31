from . import main
from datetime import datetime
from flask import render_template, session, url_for, redirect
from .forms import NameForm
from ..models import User
from .. import db
from flask import current_app
from ..emails import send_email


@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session["known"] = False
            if current_app.config["FLASKY_ADMIN"]:
                send_email(
                    current_app.config["FLASKY_ADMIN"],
                    "New User",
                    "mail/new_user",
                    user=user
                )
        else:
            session["known"] = True

        session["name"] = form.name.data

        form.name.data = ""

        return redirect(url_for(".index"))

    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        current_time=datetime.utcnow(),
        known=session.get("known", False)
    )


@main.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
