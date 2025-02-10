from flask import Flask, render_template
import requests
import random
import datetime
app = Flask(__name__)

all_posts = []
response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
for post in response.json():
    all_posts.append(post)

@app.route("/")
def index():
    print(all_posts)
    return render_template("index.html", all_posts=all_posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = [post for post in all_posts if post["id"] == post_id]
    return render_template('post.html', post=post[0])

if __name__ == "__main__":
    app.run(debug=True)
