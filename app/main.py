import random
import app.database as database
import os
from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ("DATABASE_URL")
db.init_app(app)
print("DB connect successful")


@app.route("/")
def home_view():
    return render_template('index.html')


@app.route('/insertandfind')  # , methods=["GET", "POST"])
def insertandfind():
    id = database.add_faculty(str(random.randint(0, 4564546456)), str(
        random.randint(0, 4564546456)), str(random.randint(0, 4564546456)))
    faculty = database.find_faculty_by_id(id)
    print(str(faculty.username))
    print(str(faculty.email))
    return "name" + str(str(faculty.username))