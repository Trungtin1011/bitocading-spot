import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
baseUrl = os.environ.get("BASE_URL", "/")
port = os.environ.get("PORT", "8000")
debug = os.environ.get("DEBUG", False)
listen = os.environ.get("LISTEN", "0.0.0.0")


class AppConfig:
    DATABASE = os.path.join(basedir, "board.sqlite")
    SECRET_KEY = secrets.token_hex()
