from flask import Blueprint, render_template

loader_page = Blueprint("loader_page", __name__, template_folder='templates', static_folder="static")


@loader_page.route("/post")
def index():
    return render_template('post_form.html')