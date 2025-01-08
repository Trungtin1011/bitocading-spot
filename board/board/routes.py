from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    flash,
    current_app,
)
from board.database import get_db

bp = Blueprint(
    "routes",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static",
)


@bp.route("/")
def home():
    return render_template("routes/home.html")


@bp.route("/about")
def about():
    return render_template("routes/about.html")


@bp.route("/health")
def health():
    return render_template("routes/health.html", status={"status": "OK", "code": 200})


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message),
            )
            db.commit()
            current_app.logger.info(f"New post by {author}")
            flash(f"Thanks for posting, {author}!", category="success")
            return redirect(url_for("routes.posts"))

        else:
            flash("You need to post a message.", category="error")
    return render_template("routes/create.html")


@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    ).fetchall()
    return render_template("routes/posts.html", posts=posts)
