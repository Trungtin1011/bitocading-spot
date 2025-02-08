from flask import Blueprint, flash, g, render_template, request, redirect, url_for
from landing import config
from landing.db import get_db
from landing.auth import login_required
from werkzeug.exceptions import abort

bp = Blueprint("quotes", __name__)


@bp.route("/quote", methods=["GET"])
def list_quotes():
    try:
        db = get_db()
        quotes = db.execute(
            "SELECT q.id, author_id, title, body, created, username"
            " FROM quote q JOIN user u ON q.author_id = u.id"
            " ORDER BY created DESC"
        ).fetchall()

        return render_template(
            "quotes/quotes.html", headline="Quotes For The Day", quotes=quotes
        )

    except Exception as e:
        config.logger.error(f"Failed to load quotes list with exception {e}")
        return f"Failed to load quotes list with exception {e}"


@bp.route("/quote/create", methods=("GET", "POST"))
@login_required
def create_quote():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None
        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            try:
                db = get_db()
                db.execute(
                    "INSERT INTO quote (title, body, author_id) VALUES (?, ?, ?)",
                    (title, body, g.user["id"]),
                )
                db.commit()
                config.logger.info(f"Quote '{title}' created.")
                return redirect(url_for("quotes.list_quotes"))
            except Exception as e:
                config.logger.error(f"Get error {e} when adding quote '{title}'!")
                return f"Get error {e} when adding quote '{title}'!"

    return redirect(url_for("quotes.list_quotes"))


def get_quote(id, check_author=True):
    quote = (
        get_db()
        .execute(
            "SELECT q.id, title, body, created, author_id, username"
            " FROM quote q JOIN user u ON q.author_id = u.id"
            " WHERE q.id = ?",
            (id,),
        )
        .fetchone()
    )

    if quote is None:
        abort(404, f"Quote id '{id}' doesn't exist.")

    if check_author and quote["author_id"] != g.user["id"]:
        abort(403)

    return quote


@bp.route("/quote/<int:id>/update", methods=("GET", "POST"))
@login_required
def update_quote(id):
    quote = get_quote(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            try:
                db = get_db()
                db.execute(
                    "UPDATE quote SET title = ?, body = ? WHERE id = ?",
                    (title, body, id),
                )
                db.commit()
                config.logger.info(f"Quote '{title}' updated.")
                return redirect(url_for("quotes.list_quotes"))

            except Exception as e:
                config.logger.error(f"Get error {e} when updating quote '{title}'!")
                return f"Get error {e} when updating quote '{title}'!"

    return render_template(
        "quotes/update.html", headline="Quote Modification", quote=quote
    )


@bp.route("/quote/<id>/delete")
@login_required
def delete_quote(id):
    get_quote(id)
    try:
        db = get_db()
        db.execute("DELETE FROM quote WHERE id = ?", (id))
        db.commit()
        config.logger.info(f"Quote {id} deleted.")
        return redirect(url_for("quotes.list_quotes"))

    except Exception as e:
        config.logger.error(f"Get error {e} when deleting quote '{id}'")
        return f"Get error {e} when deleting quote '{id}'"
