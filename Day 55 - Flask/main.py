from flask import Flask, render_template, request
app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'
    return wrapper

def make_underline(func):
    def wrapper(*args, **kwargs):
        return f'<u>{func(*args, **kwargs)}</u>'
    return wrapper


@app.route("/")
def index():
    return 'hello world'

@app.route("/username/<string:name>/<int:age>")
def param(name: str, age: int):
    return f"hello world {name} : age {age}"




if __name__ == "__main__":
    app.run(debug=True)
