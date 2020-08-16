import random
import app.database as database
import os
from flask import Flask, render_template, jsonify, make_response, request
import dialogflow
from app.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://dhesngxpyjyuhk:dde3232f7786335f0653d63bc3a30f2a9b8d10a29d6d5c217696d5b24415876b@ec2-52-204-20-42.compute-1.amazonaws.com:5432/d2pefa1md93jr9'
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
    
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    action = req.get('queryResult').get('action')
    if action == 'yes':
        reply = {
            "fulfillmentText": "Ok. Tickets booked successfully.",
        }
        return jsonify(reply)
    elif action == 'getdate':
        return jsonify(getAppoinmentDate(req))

@app.route('/getAppoinmentDate')
def getAppoinmentDate(req):
    date = req.get('queryResult').get('parameters').get('date')
    reply = {
        "fulfillmentText": date
    }
    return reply