import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import validators, StringField, IntegerField, SubmitField
from sqlalchemy import Integer, String, Float

# db = sqlite3.connect("books-collection.db")

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# cursor = db.cursor()

class BookForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()])
    author = StringField('Author', validators=[validators.DataRequired()])
    rating = IntegerField('Rating', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')

class Book(db.Model):
  __tablename__ = 'books'
  id = db.Column(db.Integer, primary_key=True)
  title: Mapped[str]
  author: Mapped[str]
  rating: Mapped[float]

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", all_books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        rating = form.rating.data

        book = Book(id=None, title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html", form=form)


@app.route("/book/<int:book_id>", methods=['GET'])
def book(book_id):
    book = db.session.query(Book).get_or_404(book_id)
    if book is None:
        return redirect(url_for('home'))

    return render_template("book.html", book=book)



@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book = db.session.query(Book).get_or_404(book_id)
    print(book.title)
    if book is None:
        return redirect(url_for('home'))
    form = BookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('book', book_id=book_id))

    form.title.data = book.title
    form.author.data = book.author
    form.rating.data = int(book.rating)
    return render_template("add.html", form=form)

@app.route("/delete/<int:book_id>", methods=['POST'])
def delete(book_id):
    book = db.session.query(Book).get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)


