from flask import Flask
from appboard.config import environment_variables
from appboard import routes

app = Flask(__name__)
app.register_blueprint(routes.bp, url_prefix=environment_variables["prefix"])
