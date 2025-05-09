from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_assets import Environment, Bundle
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


class ApiForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Search")


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


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    map_url: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)
    has_sockets: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    can_take_calls: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    has_toilet: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    seats: Mapped[str] = mapped_column(String, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String, nullable=True)

    from typing import Optional

    def __init__(
        self,
        name: Optional[str] = None,
        map_url: Optional[str] = None,
        img_url: Optional[str] = None,
        location: Optional[str] = None,
        has_sockets: bool = False,
        can_take_calls: bool = False,
        has_toilet: bool = False,
        has_wifi: bool = False,
        seats: Optional[str] = None,
        coffee_price: Optional[str] = None,
    ):
        self.name = name if name is not None else ""
        self.map_url = map_url if map_url is not None else ""
        self.img_url = img_url if img_url is not None else ""
        self.location = location if location is not None else ""
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.seats = seats if seats is not None else ""
        self.coffee_price = coffee_price if coffee_price is not None else ""


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
assets = Environment(app)
Bootstrap5(app)
assets.register("asset_css", css)
db.init_app(app)
# CREATE TABLE

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    return render_template("index.html", cafes=cafes)


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


@app.route("/add_api", methods=["GET", "POST"])
def add_movie_api():
    form = ApiForm()
    if form.validate_on_submit():
        title = form.title.data
        url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(
            url=url,
            params={
                "query": title,
            },
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer " + os.environ["TMDB_API_TOKEN"],
            },
        )
        return render_template("select.html", movies=response.json()["results"])
    return render_template("add.html", form=form)


@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id):
    cafe = db.session.query(Cafe).get_or_404(cafe_id)
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    return render_template("cafe.html", cafe=cafe, cafes=cafes)


# @app.route("/add_from_api/<int:movie_id>", methods=["POST"])
# def add_from_api(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     response = requests.get(
#         url=url,
#         headers={
#             "Accept": "application/json",
#             "Authorization": "Bearer " + os.environ["TMDB_API_TOKEN"],
#         },
#     )

#     movie = response.json()

#     movie = Movie(
#         id=movie_id,
#         title=movie["title"],
#         release_date=movie["release_date"],
#         review="",
#         overview=movie["overview"],
#         rating=movie["vote_average"],
#         ranking=0,
#         img_url=f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
#     )
#     db.session.add(movie)
#     db.session.commit()
#     return redirect(url_for("edit_movie", movie_id=movie_id))


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
