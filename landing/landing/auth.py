from flask import (
    Blueprint,
    flash,
    g,
    render_template,
    request,
    redirect,
    session,
    url_for,
)
from landing import config
from landing.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
import functools

bp = Blueprint("auth", __name__)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@bp.route("/auth/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
                config.logger.info(f"User '{username}' created!")
            except db.IntegrityError:
                error = f"User '{username}' is already registered."
                config.logger.error(f"User '{username}' is already registered.")
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html", headline="User Registration")


@bp.route("/auth/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            config.logger.info(f"User '{username}' logged in.")
            return redirect(url_for("landing.home"))

        flash(error)

    return render_template("auth/login.html", headline="User Login")


@bp.route("/auth/logout")
def logout():
    session.clear()
    config.logger.info("Current user logged out.")
    return redirect(url_for("landing.home"))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
