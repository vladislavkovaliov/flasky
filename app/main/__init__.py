from flask import Blueprint
from flask_login import login_required

from ..decorators import admin_required, permission_required
from ..models import Permission

main = Blueprint('main', __name__)

from . import views, errors


@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return 'for admin only!'


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return 'for moderator only!'


def inject_permissions():
    return dict(Permission=Permission)
