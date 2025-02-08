from flask import Flask, url_for
from landing import config, landing, auth, todo, db, quotes, taskflow


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config.AppConfig)

    db.init_app(app)

    app.register_blueprint(landing.bp, url_prefix=config.baseUrl)
    app.register_blueprint(auth.bp, url_prefix=config.baseUrl)
    app.register_blueprint(todo.bp, url_prefix=config.baseUrl)
    app.register_blueprint(quotes.bp, url_prefix=config.baseUrl)
    app.register_blueprint(taskflow.bp, url_prefix=config.baseUrl)

    # app.add_url_rule("/", endpoint="index") # Set default path to be used as url_for('index')

    with app.test_request_context():
        config.logger.info(
            f"Application endpoint serving at: {url_for('landing.home')}"
        )

    return app
