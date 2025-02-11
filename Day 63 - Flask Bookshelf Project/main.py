from flask import Flask, render_template, request, redirect, url_for
import sqlite3
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

@app.route('/')
def home():
    db = sqlite3.connect("books-collection.db")
    cursor = db.cursor()
    books = cursor.execute("SELECT * FROM books").fetchall()
    print(books)
    return render_template("index.html", all_books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        db = sqlite3.connect("books-collection.db")
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO books('title', 'author', 'rating') VALUES('{title}', '{author}', '{rating}')")
        db.commit()
        return redirect(url_for('home'))

    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)

