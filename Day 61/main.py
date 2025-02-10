from urllib import request
from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
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
bootstrap = Bootstrap4(app)
app.secret_key = "some secret string"
class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4, max=56)])
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.password.data == "123456789" and login_form.email.data == "admin@email.com":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)




if __name__ == '__main__':
    app.run(debug=True)
