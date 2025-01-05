from flask import Flask
from todo.config import DBConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # , static_folder="static")
app.config.from_object(DBConfig)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

from todo import routes
