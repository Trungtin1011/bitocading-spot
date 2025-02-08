from flask import Blueprint, flash, g, render_template, request, redirect, url_for
from landing import config
from landing.db import get_db
from landing.auth import login_required
from werkzeug.exceptions import abort

bp = Blueprint("taskflow", __name__)


@bp.route("/taskflow", methods=["GET"])
def tasks():
    return render_template("taskflow/taskflow.html", headline="Tasks Management")
