from todo import app, db
from todo.config import environment_variables

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(
        debug=bool(environment_variables["debug"]),
        host="0.0.0.0",
        port=int(environment_variables["port"]),
    )
