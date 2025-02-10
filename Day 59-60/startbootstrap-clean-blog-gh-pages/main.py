from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv('../../.env')

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

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("EMAIL_KEY"))
            connection.sendmail(
                from_addr=os.getenv("MY_EMAIL"),
                to_addrs="budget4you.cc@gmail.com",
                msg=f"Subject:Blog contact message\n\n{name}<br/><br/>{email}<br/><br/>{phone}<br/><br/>{message}"
            )

        return "<h1>Message sent</h1>"


@app.route("/post/<int:post_id>")
def post(post_id):
    post = [post for post in all_posts if post["id"] == post_id]
    return render_template('post.html', post=post[0])

if __name__ == "__main__":
    app.run(debug=True)
