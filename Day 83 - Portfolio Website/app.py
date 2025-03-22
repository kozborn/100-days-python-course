from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)


@app.context_processor
def inject_now():
    return {"now": datetime.utcnow()}


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
