from flask import Blueprint, render_template

main_page = Blueprint("main_page", __name__, template_folder='templates', static_folder="static")


@main_page.route("/")
@main_page.route("/home")
def index():
    return render_template('index.html')