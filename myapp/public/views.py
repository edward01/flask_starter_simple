from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

blueprint = Blueprint("public", __name__)


@blueprint.route("/landing/")
def landing():
    return render_template('public/landing.html')


@blueprint.route("/about/")
def about():
    return render_template("public/about.html")
