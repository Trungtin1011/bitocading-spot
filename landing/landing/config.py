import os
import secrets
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
baseUrl = os.environ.get("BASE_URL", "/")
port = os.environ.get("PORT", "8000")
debug = os.environ.get("DEBUG", False)
listen = os.environ.get("LISTEN", "0.0.0.0")
loglevel = os.environ.get("LEVEL", "INFO")


class AppConfig:
    DATABASE = os.path.join(basedir, "landing.sqlite")
    SECRET_KEY = secrets.token_hex()


# Init logger
# logging.basicConfig(format="[%(levelname)s]\t%(message)s", level=logging.INFO)
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=getattr(logging, loglevel.upper(), logging.INFO),
)
logging.getLogger("werkzeug").disabled = True
logger = logging.getLogger()
