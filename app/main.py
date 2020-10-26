from flask import Blueprint, render_template, request
from .algorithm import recursion_sum

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        old_value = request.form["flask_value"]
        if old_value:
            value = recursion_sum(old_value)

            return render_template("index.html", show=True, value=value, old_value=old_value)

    return render_template("index.html", old_value="")
