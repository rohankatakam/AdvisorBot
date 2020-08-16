from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BINARY, Table, Column, Integer, ForeignKey, DATE, TIMESTAMP, BOOLEAN, Text

db = SQLAlchemy()

# class Roles(db.Model):
#     roleid = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
#     rolename = db.Column(db.String(), nullable=False)

class Faculties(db.Model):
    facultyid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.BINARY(64))
    salt = db.Column(db.BINARY(64))
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    # roleid = db.Column(db.Integer, ForeignKey(Roles.roleid))

class Departments(db.Model):
    departmentid = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    departmentname = db.Column(db.Text, nullable=False)

class DepartmentRecords(db.Model):
    facultyid = db.Column(db.Integer, ForeignKey(Faculties.facultyid), nullable=False, primary_key=True)
    departmentid = db.Column(db.Integer, ForeignKey(Departments.departmentid), nullable=False, primary_key=True)

class Majors(db.Model):
    majorid = db.Column(db.Integer, nullable=False, primary_key=True)
    departmentid = db.Column(db.Integer, ForeignKey(Departments.departmentid), nullable=False, primary_key=True)
    majorname = db.Column(db.Text, nullable=False)

class AppointmentRecords(db.Model):
    appointmentid = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    appointmentdate = db.Column(db.Date, nullable=False)
    appointmentstartTime = db.Column(db.TEXT, nullable=False)
    appointmentendTime = db.Column(db.TEXT, nullable=False)
    appointmenttopic = db.Column(db.Text, nullable=False)
    appointmentcomment = db.Column(db.Text)
    facultyid = db.Column(db.Integer, ForeignKey(Faculties.facultyid), nullable=False)
    studentid = db.Column(db.Integer, nullable=True)
    studentemail = db.Column(db.Text, nullable=False)
    studentfirstname = db.Column(db.Text)
    studentlastname = db.Column(db.Text)
    majorid = db.Column(db.Integer, ForeignKey(Majors.majorid))
    departmentid = db.Column(db.Integer, ForeignKey(Departments.departmentid))

class TicketRecords(db.Model):
    ticketid = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    studentid = db.Column(db.Date, nullable=True)
    time = db.Column(db.TEXT, nullable=False)
    tickettitle = db.Column(db.Text)
    ticketcontent = db.Column(db.Text)
    solved = db.Column(db.BOOLEAN, nullable=False)
    advisorid = db.Column(db.Integer, ForeignKey(Faculties.facultyid))
    studentfirstname = db.Column(db.Text)
    studentlastname = db.Column(db.Text)
    studentemail = db.Column(db.Text, nullable=False)
    departmentid = db.Column(db.Integer, ForeignKey(Departments.departmentid))
    majorid = db.Column(db.Integer, ForeignKey(Majors.majorid))




