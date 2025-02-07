from flask import Flask, render_template, request
import random
app = Flask(__name__)

NUMBER = random.randint(0, 10)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return wrapper

@app.route("/")
def index():
    return '<div>Guess a number between 0 and 9!</div><div>Add a number to url like this: <u>http://127.0.0.1:5000/number</u></div>'

@app.route("/<int:number>")
def param(number):
    if number > NUMBER:
        return "<div><h1>TOO HIGH</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' /></div>"
    elif number < NUMBER:
        return "<div><h1>TOO LOW</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' /></div>"
    else:
        return "<div><h1>CORRECT</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' /></div>"


if __name__ == "__main__":
    app.run(debug=True)
