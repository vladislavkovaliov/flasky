from flask import Blueprint
from flask_login import login_required

from ..decorators import admin_required
from ..models import Permission

main = Blueprint("main", __name__)

from . import views, errors


@main.route("/admin")
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"


@main.route("/moderator")
@login_required
@admin_required
def for_moderators_only():
    return "For comment moderators!"


def inject_permissions():
    return dict(Permission=Permission)
