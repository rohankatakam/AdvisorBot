import random
import app.database as database
import os
from flask import Flask, render_template, jsonify, make_response, request, redirect
from app.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://dhesngxpyjyuhk:dde3232f7786335f0653d63bc3a30f2a9b8d10a29d6d5c217696d5b24415876b@ec2-52-204-20-42.compute-1.amazonaws.com:5432/d2pefa1md93jr9'
db.init_app(app)
print("DB connect successful")

@app.route("/")
def home_view():
    return render_template('index.html')

@app.route("/advisor-login", methods=["GET", "POST"])
def advisor_login():
    if request.method == 'GET':
        return render_template('advisor-login.html')
    else:
        email = request.form['email']
        password = request.form['password']

        ## MARCO ADD DATABASE LOG IN RIGHT HERE
        #database.add_faculty(username, email, password, firstname, lastname)
        status = database.emaillogin(email, password)
        return render_template('advisor-login.html', eml=email, pswd= password, callbackmsg=" successfully logged in!" if status else " failed to log in!")

@app.route("/advisor-signup", methods=["GET", "POST"])
def advisor_signup():
    if request.method == 'GET':
        return render_template('advisor-signup.html')
    else:
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        ## MARCO ADD DATABASE SIGN UP RIGHT HERE
        #database.add_faculty(username, email, password, firstname, lastname)
        database.add_faculty(username,email,password,firstname,lastname)
        return render_template('advisor-signup.html', usrnme=username, fstnme= firstname, lstnme= lastname, callbackmsg=" registered!")
        



@app.route('/insertandfind')  # , methods=["GET", "POST"])
def insertandfind():
    # id = database.add_faculty(str(random.randint(0, 4564546456)), str(
    #     random.randint(0, 4564546456)), str(random.randint(0, 4564546456)))
    # faculty = database.find_faculty_by_id(id)
    # print(str(faculty.username))
    # print(str(faculty.email))
    # did = database.add_department("UW CSE")
    # fid = database.add_faculty("asd","asdasd","asd","a","sd")
    # drid = database.add_department_record(
    #     database.find_faculty_by_username("asd").facultyid,\
    #     database.find_department_by_name("UW CSE").departmentid)
    # mid = database.add_major("CS", database.find_department_by_name("UW CSE").departmentid)
    # database.add_appointment("Asdasd", fid, mid, did, "2020-08-16", "10:00:00", "ddd", "ssss", "asd", "asd")
    # print(str(database.find_appointment_slots(did, "2020-08-16")))
    # return str(database.find_appointment_slots(did, "2020-08-16"))
    return "bang"
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
