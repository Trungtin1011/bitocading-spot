import os
from flask import Flask, url_for
from flaskr import db, auth, blog


# Ref: https://flask.palletsprojects.com/en/stable/tutorial/factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    app.logger.setLevel("INFO")
    db.init_app(app)
    app.register_blueprint(auth.bp, url_prefix="/flaskr")
    app.register_blueprint(blog.bp, url_prefix="/flaskr")
    # app.add_url_rule("/", endpoint="index") # Set default path to be used as url_for('index')

    with app.test_request_context():
        app.logger.info(f"Main endpoint serving at: {url_for('blog.index')}")
        app.logger.info(f"Create blog endpoint serving at: {url_for('blog.create')}")
        app.logger.info(
            f"User registration endpoint serving at: {url_for('auth.register')}"
        )
        app.logger.info(f"User login endpoint serving at: {url_for('auth.login')}")

    return app
