from appboard import app
from appboard.config import environment_variables

if __name__ == "__main__":
    app.run(
        debug=bool(environment_variables["debug"]),
        host="0.0.0.0",
        port=int(environment_variables["port"]),
    )
