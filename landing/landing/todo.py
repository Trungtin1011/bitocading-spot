from flask import Blueprint, flash, render_template, request, redirect, url_for
from landing import config
from landing.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint("todo", __name__)


@bp.route("/todo", methods=["GET"])
def list_tasks():
    try:
        db = get_db()
        todos = db.execute(
            "SELECT id, title, complete, created FROM task ORDER BY created DESC"
        ).fetchall()

        return render_template("todo/todo.html", headline="Todo Tasks", todos=todos)

    except Exception as e:
        config.logger.error(f"Failed to load todo list with exception {e}")
        return f"Failed to load todo list with exception {e}"


@bp.route("/todo/add", methods=["POST"])
def add():
    item = request.form["todoitem"]
    error = None
    if item == "":
        error = "Cannot add new task, empty input received!"
        config.logger.error("Cannot add new task, empty input received!")

    if error is not None:
        flash(error)
    else:
        try:
            db = get_db()
            db.execute("INSERT INTO task (title, complete) VALUES (?, ?)", (item, 0))
            db.commit()
            config.logger.info(f"New task '{item}' added.")
            return redirect(url_for("todo.list_tasks"))
        except Exception as e:
            config.logger.error(f"Get error {e} when adding task '{item}'!")
            return f"Get error {e} when adding task '{item}'!"

    return redirect(url_for("todo.list_tasks"))


def get_task(id):
    task = get_db().execute("SELECT title FROM task WHERE id = ?", (id)).fetchone()

    if task is None:
        abort(404, f"Post id {id} doesn't exist.")

    return task[0]


@bp.route("/todo/complete/<id>")
def complete(id):
    task = get_task(id)
    try:
        db = get_db()
        db.execute("UPDATE task SET complete = ? WHERE id = ?", (1, id))
        db.commit()

        config.logger.info(f"Task '{task}' completed!")
        return redirect(url_for("todo.list_tasks"))

    except Exception as e:
        config.logger.error(f"Get error {e} when updating task '{task}'!")
        return f"Get error {e} when updating task '{task}'!"


@bp.route("/todo/undone/<id>")
def undone(id):
    task = get_task(id)
    try:
        db = get_db()
        db.execute("UPDATE task SET complete = ? WHERE id = ?", (0, id))
        db.commit()

        config.logger.info(f"Task '{task}' undone!")
        return redirect(url_for("todo.list_tasks"))

    except Exception as e:
        config.logger.error(f"Get error {e} when updating task '{task}'!")
        return f"Get error {e} when updating task '{task}'!"


@bp.route("/todo/delete/<id>")
def delete(id):
    task = get_task(id)

    try:
        db = get_db()
        db.execute("DELETE FROM task WHERE id = ?", (id))
        db.commit()
        config.logger.info(f"Task '{task}' deleted!")
        return redirect(url_for("todo.list_tasks"))

    except Exception as e:
        config.logger.error(f"Get error {e} when deleting task '{task}'")
        return f"Get error {e} when deleting task '{task}'"
