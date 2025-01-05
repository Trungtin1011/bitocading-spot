import os
import logging

# Init common environment variables
environment_variables = {
    "basedir": os.path.abspath(os.path.dirname(__file__)),
    "dbtype": os.environ.get("DB_TYPE", "sqlite"),
    "db_user": os.environ.get("DB_USER", ""),
    "db_pwd": os.environ.get("DB_PWD", ""),
    "db_host": os.environ.get("DB_HOST", ""),
    "db_name": os.environ.get("DB_NAME", ""),
    "port": os.environ.get("PORT", "8080"),
    "debug": os.environ.get("DEBUG", False),
    "app_title": os.environ.get("TITLE", "To-Do"),
    "app_heading": os.environ.get("HEADLINE", "To-do tasks Flask application"),
    "loglevel": os.environ.get("LOG_LEVEL", "INFO"),
}

# Init logger
# logging.basicConfig(format="[%(levelname)s]\t%(message)s", level=logging.INFO)
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=getattr(logging, environment_variables["loglevel"].upper(), logging.INFO),
)
logging.getLogger("werkzeug").disabled = True
logger = logging.getLogger()


class DBConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if environment_variables["dbtype"] == "sqlite":
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
            environment_variables["basedir"], "todo.db"
        )
    else:
        SQLALCHEMY_DATABASE_URI = (
            "{dbtype}://{username}:{password}@{hostname}/{databasename}".format(
                dbtype=environment_variables["dbtype"],
                username=environment_variables["db_user"],
                password=environment_variables["db_pwd"],
                hostname=environment_variables["db_host"],
                databasename=environment_variables["db_name"],
            )
        )
