from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint("landing", __name__)


@bp.route("/")
def home():
    return render_template("landing/home.html", headline="Applications Landing")


@bp.route("/about")
def about():
    return render_template("landing/about.html", headline="About")


@bp.route("/health")
def health():
    return render_template(
        "landing/health.html",
        headline="Health Report",
        status={"status": "OK", "code": 200},
    )
