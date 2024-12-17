from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/create_post")
def create_post():
    return render_template("create_post.html")


@app.route("/posts")
def posts():
    return render_template("posts.html")


if __name__ == "__main__":
    app.run(debug=True)