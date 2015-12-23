from flask import Blueprint, request, render_template, url_for

main_editor = Blueprint("editor", __name__)

@main_editor.route("/", methods=["GET"])
def render_editor():
    return render_template("editor/main.html")

