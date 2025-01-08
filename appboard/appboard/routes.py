from flask import Blueprint, render_template, jsonify, send_from_directory
from appboard.config import logger, environment_variables, loadConfig

bp = Blueprint(
    "routes",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static",
)
title = environment_variables["app_title"]
heading = environment_variables["app_heading"]


@bp.route("/")
def index():
    try:
        appCats = loadConfig()
        return render_template(
            "index.html",
            title=title,
            headline=heading,
            categories=appCats,
        )
    except Exception as e:
        logger.error(f"Failed to load AppBoard with exception {e}")
        return f"Failed to load AppBoard with exception {e}"


@bp.route("/health")
def health_check():
    return jsonify({"status": "ok", "code": 200})


@bp.route("/icons/<path:icon>")
def icons(icon):
    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory(environment_variables["icon_dir"], icon)
