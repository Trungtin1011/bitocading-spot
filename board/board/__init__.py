from flask import Flask, url_for
from board import routes, database, errors, config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.AppConfig)
    app.logger.setLevel("INFO")

    database.init_app(app)

    app.register_blueprint(routes.bp, url_prefix=config.baseUrl)
    app.register_error_handler(404, errors.page_not_found)

    with app.test_request_context():
        app.logger.info(f"Main endpoint serving at: {url_for('routes.home')}")
        app.logger.info(f"About page serving at: {url_for('routes.about')}")
        app.logger.info(f"Healthcheck page serving at: {url_for('routes.health')}")
        app.logger.info(f"Posts view serving at: {url_for('routes.posts')}")
        app.logger.info(f"Posts create serving at: {url_for('routes.create')}")

    return app
