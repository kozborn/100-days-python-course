from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    abort,
    jsonify,
)
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_assets import Environment, Bundle
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
import requests
from dotenv import load_dotenv
import os

load_dotenv("../.env")

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


css = Bundle(
    "src/scss/main.scss",  # Path to your main SCSS file (inside static folder)
    filters="libsass",
    output="dist/css/styles.css",  # Output CSS file
    depends="src/scss/*.scss",  # Rebuild if any SCSS file changes
)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    todo_items = relationship("TodoItem", back_populates="author")

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


class TodoItem(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, unique=False)
    done: Mapped[bool] = mapped_column(db.Boolean, default=False, nullable=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="todo_items")

    from typing import Optional

    def __init__(
        self,
        text: Optional[str] = None,
        done: Optional[bool] = False,
        author: Optional[User] = None,
    ):
        self.text = text if text is not None else ""
        self.done = done if done is not None else False
        self.author = author if author is not None else None
        self.author_id = author.id


class TodoItemForm(FlaskForm):
    text = StringField("Text", validators=[DataRequired()])
    done = BooleanField("Done")
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
assets = Environment(app)
login_manager = LoginManager()
login_manager.init_app(app)


Bootstrap5(app)
assets.register("asset_css", css)
db.init_app(app)
# CREATE TABLE

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=["GET", "POST"])
def home():
    form = TodoItemForm()
    if current_user.is_authenticated:
        todo_list = (
            TodoItem.query.filter_by(author_id=current_user.id)
            .order_by(TodoItem.id.desc())
            .all()
        )
        if request.method == "POST":
            print("POST")

            if form.validate_on_submit():

                todo_item = TodoItem(
                    text=form.text.data,
                    done=form.done.data,
                    author=current_user,
                )
                db.session.add(todo_item)
                db.session.commit()
                return redirect(url_for("home"))

    else:
        todo_list = []
    return render_template("index.html", todo_list=todo_list, form=form)


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    data = request.get_json()
    todo = TodoItem.query.get_or_404(todo_id)

    todo.done = data["done"]
    db.session.commit()
    return jsonify({"success": True, "done": todo.done})


@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
    todo = TodoItem.query.get_or_404(todo_id)
    form = TodoItemForm(
        text=todo.text,
        done=todo.done,
    )

    if request.method == "POST":
        if form.validate_on_submit():
            todo.text = form.text.data
            todo.done = form.done.data
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("edit.html", form=form, todo=todo)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if (
        request.method == "POST"
        and len(request.form["password"]) > 0
        and len(request.form["email"])
    ):
        # Login and validate the user.

        user = User.query.filter_by(email=request.form["email"]).first()
        if user and user.check_password(request.form["password"]):
            # user should be an instance of your `User` class
            login_user(user)

            flash("Logged in successfully.")

            next = request.args.get("next")
            # url_has_allowed_host_and_scheme should check if the url is safe
            # for redirects, meaning it matches the request host.
            # See Django's url_has_allowed_host_and_scheme for an example.
            # if not url_has_allowed_host_and_scheme(next, request.host):
            #     return abort(400)

            return redirect(next or url_for("home"))
        else:
            flash("Username or password incorrect.")
    return render_template("user/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = User.query.filter_by(email=request.form["email"]).first()
        if user_exists:
            flash("Email already registered")
            return redirect(url_for("login"))
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        user = User(name=name, email=email, password=generate_password_hash(password))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home", user={user}))

    return render_template("user/register.html")


@login_required
@app.route("/add", methods=["POST"])
def add_todo_item():
    form = TodoItemForm()

    if form.validate_on_submit():

        todo_item = TodoItem(
            text=form.text.data,
            done=form.done.data,
            author=current_user,
        )
        db.session.add(todo_item)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/delete/<int:todo_item_id>", methods=["POST"])
def delete_todo_item(todo_item_id):
    todo_item = db.session.query(TodoItem).get_or_404(todo_item_id)
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for("home"))


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
