from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = {}

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    for post in response.json():
        posts[post["id"]] = Post(post["id"], post["title"], post["body"])

    return render_template("index.html", posts=response.json())

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", post=posts[post_id])


if __name__ == "__main__":
    app.run(debug=True)
