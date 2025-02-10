from flask import Flask, render_template
import requests
import random
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1, 100)
    current_time = datetime.datetime.now()
    return render_template("index.html", num=random_number, year=current_time.year)

@app.route("/about/<name>")
def about(name):
    agify = requests.get(f"https://api.agify.io?name={name}")
    print(agify.json())
    genderify = requests.get(f"https://api.genderize.io?name={name}")
    print(genderify.json())

    return render_template("about.html", name=name.title(), age=agify.json()["age"], gender=genderify.json()["gender"])


@app.route("/blog")
def blog_posts():

    url ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    return render_template("blog.html", posts=response.json())

if __name__ == "__main__":
    app.run(debug=True)
