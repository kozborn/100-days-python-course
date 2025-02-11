from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os
load_dotenv("../.env")

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class ApiForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search')

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = StringField('Release date', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    ranking = IntegerField('Ranking', validators=[DataRequired()])
    review = StringField('My review', validators=[DataRequired()])
    img_url = StringField('Background image', validators=[DataRequired()])
    overview = StringField('Overview', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditMovieForm(FlaskForm):
    ranking = IntegerField('Ranking', validators=[DataRequired()])
    review = StringField('My review', validators=[DataRequired()])
    submit = SubmitField('Update')

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title: Mapped[str] = db.Column(db.String, unique=True)
  review: Mapped[str] = db.Column(db.String, nullable=True)
  ranking: Mapped[int] = db.Column(db.Integer, nullable=True)
  overview: Mapped[str] = db.Column(db.String, nullable=True)
  release_date: Mapped[str] = db.Column(db.String, nullable=True)
  rating: Mapped[float] = db.Column(db.Float, nullable=True)
  img_url: Mapped[str] = db.Column(db.String, nullable=True)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
db.init_app(app)
# CREATE TABLE

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=movies)

@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        rating = form.rating.data
        review = form.review.data
        ranking = form.ranking.data
        overview = form.overview.data
        img_url = form.img_url.data
        movie = Movie(title=title, release_date=release_date, review=review, overview=overview, rating=rating, ranking=ranking, img_url=img_url)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)


@app.route("/add_api", methods=['GET', 'POST'])
def add_movie_api():
    form = ApiForm()
    if form.validate_on_submit():
        title = form.title.data
        url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(url=url, params={
            "query": title,
        }, headers={
            "Accept": "application/json",
            "Authorization": "Bearer " + os.environ["TMDB_API_TOKEN"]
        })
        return render_template('select.html', movies=response.json()['results'])
    return render_template("add.html", form=form)

@app.route("/add_from_api/<int:movie_id>", methods=['POST'])
def add_from_api(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url=url, headers={
        "Accept": "application/json",
        "Authorization": "Bearer " + os.environ["TMDB_API_TOKEN"]
    })

    movie = response.json()

    movie = Movie(id=movie_id, title=movie['title'], release_date=movie['release_date'], review="", overview=movie['overview'], rating=movie['vote_average'],
                  ranking=0, img_url=f"https://image.tmdb.org/t/p/w185{movie['poster_path']}")
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit_movie', movie_id=movie_id))


@app.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = db.session.query(Movie).get_or_404(movie_id)
    form = EditMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.ranking = form.ranking.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route('/delete/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    movie = db.session.query(Movie).get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
