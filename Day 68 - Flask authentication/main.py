from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE

login_manager = LoginManager()
login_manager.init_app(app)

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_exists = User.query.filter_by(email=request.form['email']).first()
        if user_exists:
            flash('Email already registered')
            return redirect (url_for('login'))
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        user = User(name=name, email=email, password=generate_password_hash(password))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('secrets', user={user}))

    return render_template("register.html")


# @app.route('/login')
# def login():
#     return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if request.method == 'POST' and len(request.form['password']) > 0 and len(request.form['email']):
        # Login and validate the user.

        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            # user should be an instance of your `User` class
            login_user(user)

            flash('Logged in successfully.')

            next = request.args.get('next')
            # url_has_allowed_host_and_scheme should check if the url is safe
            # for redirects, meaning it matches the request host.
            # See Django's url_has_allowed_host_and_scheme for an example.
            # if not url_has_allowed_host_and_scheme(next, request.host):
            #     return abort(400)

            return redirect(next or url_for('secrets'))
        else:
            flash('Username or password incorrect.')
    return render_template('login.html')

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files/', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
