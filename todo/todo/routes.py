from flask import Flask, render_template, request, url_for, redirect, jsonify
from todo import app, db
from todo.models import Todo
from todo.config import logger, environment_variables


title = environment_variables["app_title"]
heading = environment_variables["app_heading"]


@app.route("/")
def index():
    # incomplete = Todo.query.filter_by(complete=False).all()
    # complete = Todo.query.filter_by(complete=True).all()
    try:
        todos = Todo.query.all()
        msg = request.args.get("msg", "Flask application initialized!")
        return render_template(
            "index.html", title=title, headline=heading, msg=msg, todos=todos
        )
    except Exception as e:
        logger.error(f"Failed to load todo list with exception {e}")
        return f"Failed to load todo list with exception {e}"


@app.route("/health")
def health_check():
    return jsonify({"status": "ok", "code": 200})


@app.route("/add", methods=["POST"])
def add():
    item = request.form["todoitem"]
    if item == "":
        logger.error("Cannot add new task, empty input received!")
        return redirect(
            url_for("index", msg="Cannot add new task, empty input received!")
        )
    else:
        todo = Todo(text=item, complete=False)

        try:
            db.session.add(todo)
            db.session.commit()
            logger.info(f"New task '{todo}' added!")
            return redirect(url_for("index", msg=f"New task '{todo}' added!"))

        except Exception as e:
            logger.error(f"Get error {e} when adding task '{todo}'!")
            return f"Get error {e} when adding task '{todo}'!"


@app.route("/complete/<id>")
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    logger.info(f"Task '{todo}' completed!")

    return redirect(url_for("index", msg=f"Task '{todo}' completed!"))


# delete a task
@app.route("/delete/<id>")
def delete(id):
    todo = Todo.query.filter_by(id=int(id)).first()

    try:
        db.session.delete(todo)
        db.session.commit()
        logger.info(f"Task '{todo}' deleted!")
        return redirect(url_for("index", msg=f"Task '{todo}' deleted!"))

    except Exception as e:
        logger.error(f"Get error {e} when deleting task '{todo}'")
        return f"Get error {e} when deleting task '{todo}'"
