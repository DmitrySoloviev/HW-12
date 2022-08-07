from flask import Flask, request, render_template, send_from_directory
from dir_main.main_file import main_page
from loader.loader import loader_page
from functions import load_post
from functions import write_in_file

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.register_blueprint(main_page)
app.register_blueprint(loader_page)

@app.route("/search")
def search_page():
    s = request.args['s']
    post_dict = load_post('posts.json', s)
    pic_for_post = post_dict["pic"]
    cont_for_post = post_dict["content"]
    return render_template('post_list.html', picture=pic_for_post, contents=cont_for_post, user_search=s)

@app.route("/")
def page_index():
    pass


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass

@app.route('/add', methods=["POST"])
def add_page():
    new_content = request.form['new_content']
    new_picture = request.files.get("new_picture")
    filename = new_picture.filename
    new_picture.save(f"./uploads/images/{filename}")
    file_path = f"./uploads/images/{filename}"
    write_in_file(file_path, new_content)
    return render_template('post_uploaded.html', new_content=new_content, new_picture=filename)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

