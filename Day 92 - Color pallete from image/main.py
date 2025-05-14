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
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from PIL import Image

from werkzeug.security import generate_password_hash, check_password_hash
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


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField("Upload Photo")


css = Bundle(
    "src/scss/main.scss",  # Path to your main SCSS file (inside static folder)
    filters="libsass",
    output="dist/css/styles.css",  # Output CSS file
    depends="src/scss/*.scss",  # Rebuild if any SCSS file changes
)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
assets = Environment(app)

Bootstrap5(app)
assets.register("asset_css", css)


def resize_image(width, height, threshold):
    """
    Function takes in an image's original dimensions and returns the
    new width and height while maintaining its aspect ratio where
    both are below the threshold. Purpose is to reduce runtime and
    not distort the original image too much.

    Parameters
    ----------
    width : int
        original width of image
    height : int
        original height of image
    threshold : int
        max dimension size for both width and height
    """
    if (width > threshold) or (height > threshold):
        max_dim = max(width, height)
        if height == max_dim:
            new_width = int((width * threshold) / height)
            new_height = threshold
        if width == max_dim:
            new_height = int((height * threshold) / width)
            new_width = threshold
        return new_width, new_height
    else:
        return width, height


def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def detect_colors(image_path):
    """
    Function returns colors detected in image.

    Parameters
    ----------
    image_path : str
        path to imagefile for detection

    Return
    ------
    sorted list of tuples (color, total number detections)
    """

    # Read image
    image = Image.open(image_path)

    # Convert image into RGB
    image = image.convert("RGB")
    # Get width and height of image
    width, height = image.size
    print(f"Original dimensions: {width} x {height}")
    color_resolution = (
        25  # Resolution of color detection, lower means more colors detected
    )
    # Resize image to improve runtime
    width, height = resize_image(width, height, threshold=50)
    print(f"New dimensions: {width} x {height}")
    image = image.resize((width, height))

    # Iterate through each pixel
    detected_colors = {}  # hash-map
    for x in range(0, width):
        for y in range(0, height):
            # r,g,b value of pixel
            r, g, b = image.getpixel((x, y))

            r_rounded = round(r / color_resolution) * color_resolution
            g_rounded = round(g / color_resolution) * color_resolution
            b_rounded = round(b / color_resolution) * color_resolution

            # Ensure values stay within 0-255 range
            r_rounded = min(255, max(0, r_rounded))
            g_rounded = min(255, max(0, g_rounded))
            b_rounded = min(255, max(0, b_rounded))

            rgb = f"{r_rounded},{g_rounded},{b_rounded}"

            if rgb in detected_colors:
                detected_colors[rgb] += 1
            else:
                detected_colors[rgb] = 1

    # Sort colors from most common to least common
    detected_colors = sorted(detected_colors.items(), key=lambda x: x[1], reverse=True)

    return detected_colors


@app.route("/", methods=["GET", "POST"])
def home():
    form = PhotoForm()
    colors = []
    filename = None
    if form.validate_on_submit():
        # Handle file upload
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        path_to_file = os.path.join("static", "uploads", filename)
        photo.save(path_to_file)
        flash("Photo uploaded successfully!", "success")
        print(f"File saved as: {path_to_file}")
        colors = detect_colors(path_to_file)
        # Handle form submission or other POST requests here
        # For example, you can save the filename to the database or process it further
        return render_template(
            "index.html", form=form, colors=colors, filename=filename
        )

    # Render the home page

    return render_template("index.html", form=form, colors=colors, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
