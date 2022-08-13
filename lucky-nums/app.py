from flask import Flask, render_template, request, jsonify

from models import db, connect_db, User
import requests
import random

API_BASE_URL = "http://numbersapi.com/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "mishacat123"

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=["POST"])
def lucky_num():
    user = User(name=request.json['name'],
                email=request.json['email'],
                year=request.json['year'],
                color=request.json['color'],
                lucky_num=random.randrange(1, 101, 1))

    db.session.add(user)
    db.session.commit()

    year_fact = requests.get(
        f"{API_BASE_URL}/{user.lucky_num}/{user.year}?json").text
    num_fact = requests.get(f"{API_BASE_URL}/{user.lucky_num}?json").text

    response_json = jsonify(num={'num': f'{user.lucky_num}', 'fact': f'{num_fact}'}, year={
                            'year': f'{user.year}', 'fact': f'{year_fact}'})

    return (response_json, 201)
