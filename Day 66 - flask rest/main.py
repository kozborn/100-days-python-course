from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import func, select
from sqlalchemy.orm import load_only
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/all")
def all_cafes():
   cafes = Cafe.query.order_by(Cafe.name).all()
   cafes_dict = [cafe.to_dict() for cafe in cafes]

   return jsonify(cafes_dict)


@app.route('/random')
def random_route():
    cafe = Cafe.query.order_by(func.random()).first()
    # return jsonify(cafe={
    #     "name":cafe.name,
    #     "map_url":cafe.map_url,
    #     "img_url":cafe.img_url,
    #     "location":cafe.location,
    #     "seats":cafe.seats,
    #     "has_toilet":cafe.has_toilet,
    #     "coffee_price":cafe.coffee_price,
    #     "can_take_calls":cafe.can_take_calls,
    #     "has_wifi":cafe.has_wifi,
    #     "has_sockets":cafe.has_sockets
    # })

    return jsonify(cafe.to_dict())

@app.route('/search')
def search_route():
    loc = request.args.get('loc')
    if loc is None:
        return jsonify([])
    cafes = db.session.execute(select(Cafe).where(Cafe.name.like('%'+loc+'%'))).scalars()
    if cafes:
        return jsonify([c.to_dict() for c in cafes])
    else:
        return jsonify([

        ])



# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    cafes = Cafe.query.order_by(Cafe.id).all()
    if request.method == 'GET':
        return jsonify([c.to_dict() for c in cafes])
    elif request.method == 'POST':
        # new_cafe = Cafe(
        #     name=request.json.get('name'),
        #     map_url=request.json.get('map_url') or "",
        #     img_url=request.json.get('img_url') or "",
        #     location=request.json.get('location') or "",
        #     seats=request.json.get('seats') or "",
        #     has_toilet=bool(request.json.get('has_toilet')),
        #     has_wifi=bool(request.json.get('has_wifi')),
        #     has_sockets=bool(request.json.get('has_sockets')),
        #     can_take_calls=bool(request.json.get('can_take_calls')),
        #     coffee_price=request.json.get('coffee_price') or ""
        # )

        new_cafe = Cafe(
            name=request.form.get('name'),
            img_url=request.form.get('img_url') or "",
            seats=request.form.get('seats') or "",
            map_url=request.form.get('map_url') or "",
            location=request.form.get('location') or "",
            has_toilet=bool(request.form.get('has_toilet')),
            has_wifi=bool(request.form.get('has_wifi')),
            has_sockets=bool(request.form.get('has_sockets')),
            can_take_calls=bool(request.form.get('can_take_calls')),
            coffee_price=request.form.get('coffee_price') or ""
        )

        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({
            "response": {
                "status": "Success"
            }
        })

# HTTP PUT/PATCH - Update Record

@app.route('/cafes/<int:cafe_id>', methods=['GET', 'PATCH', 'DELETE'])
def cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify({"response": {"error": "No such cafe"}}), 404
    if request.method == 'GET':
        return jsonify(cafe.to_dict())
    elif request.method == 'PATCH':
        cafe_req = {
            "name": request.form.get('name'),
            "img_url": request.form.get('img_url'),
            "seats": request.form.get('seats'),
            "map_url": request.form.get('map_url'),
            "location": request.form.get('location'),
            "has_toilet": request.form.get('has_toilet'),
            "has_wifi": bool(request.form.get('has_wifi')) if request.form.get('has_wifi') else None,
            "has_sockets": bool(request.form.get('has_sockets')) if request.form.get('has_sockets') else None,
            "can_take_calls": bool(request.form.get('can_take_calls')) if request.form.get('can_take_calls') else None,
            "coffee_price": request.form.get('coffee_price')
        }
        cafe_req = {k: v for k, v in cafe_req.items() if v is not None}
        for k, v in cafe_req.items():
            setattr(cafe, k, v)
        db.session.commit()
        return jsonify({"response": {"status": "Updated"}})
    elif request.method == 'DELETE':
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"response": {"status": "Deleted"}})



# HTTP DELETE - Delete Record




if __name__ == '__main__':
    app.run(debug=True)
