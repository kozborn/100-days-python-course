from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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


class CafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired()])
    img_url = StringField("Img  URL", validators=[DataRequired()])
    has_wifi = BooleanField("Has WiFi")
    can_take_calls = BooleanField("Can take calls")
    has_sockets = BooleanField("Has Sockets")
    has_toilet = BooleanField("Has Toilet")
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    submit = SubmitField("Submit")


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, unique=False)
    done: Mapped[bool] = mapped_column(db.Boolean, default=False, nullable=True)
    user_id: Mapped[int] = mapped_column(
        Integer, db.ForeignKey("user.id"), nullable=True
    )

    from typing import Optional

    def __init__(
        self,
        text: Optional[str] = None,
        done: Optional[bool] = False,
    ):
        self.text = text if text is not None else ""
        self.done = done if done is not None else False


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


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

            return redirect(next or url_for("secrets"))
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
        return redirect(url_for("secrets", user={user}))

    return render_template("user/register.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():

        cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            can_take_calls=form.can_take_calls.data,
            has_wifi=form.has_wifi.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
            img_url=form.img_url.data,
        )
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id):
    cafe = db.session.query(Cafe).get_or_404(cafe_id)
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    return render_template("cafe.html", cafe=cafe, cafes=cafes)


@app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe = db.session.query(Cafe).get_or_404(cafe_id)
    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.map_url = form.map_url.data
        cafe.location = form.location.data
        cafe.has_sockets = form.has_sockets.data
        cafe.has_toilet = form.has_toilet.data
        cafe.can_take_calls = form.can_take_calls.data
        cafe.has_wifi = form.has_wifi.data
        cafe.seats = form.seats.data
        cafe.coffee_price = form.coffee_price.data
        cafe.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", cafe=cafe, form=form)


@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
