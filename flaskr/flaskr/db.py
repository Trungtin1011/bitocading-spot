import sqlite3
from datetime import datetime
from flask import current_app, g


# Ref: https://flask.palletsprojects.com/en/stable/tutorial/database
def init_app(app):
    app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command)
    with app.app_context():
        init_db_command()


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db_command():
    """Clear the existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    current_app.logger.info("Initialized the database.")


sqlite3.register_converter("timestamp", lambda v: datetime.fromisoformat(v.decode()))
