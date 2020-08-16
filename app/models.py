from app import db
from sqlalchemy import BINARY, Table, Column, Integer, ForeignKey, DATE, TIMESTAMP, BOOLEAN

class Roles(db.Model):
    roleId = db.Column(db.Integer, nullable=False, primary_key=True)
    roleName = db.Column(db.String(), nullable=False)

class Faculties(db.Model):
    facultyId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.BINARY(64))
    salt = db.Column(db.BINARY(64))
    roleId = db.Column(db.Integer, ForeignKey(Roles.roleId))

class Departments(db.Model):
    departmentId = db.Column(db.Integer, nullable=False, primary_key=True)
    departmentName = db.Column(db.String(20), nullable=False)

class DepartmentRecords(db.Model):
    facultyId = db.Column(db.Integer, ForeignKey(Faculties.facultyId), nullable=False)
    departmentId = db.Column(db.Integer, ForeignKey(Departments.departmentId), nullable=False)

class Majors(db.Model):
    majorId = db.Column(db.Integer, nullable=False, primary_key=True)
    majorName = db.Column(db.String(50), nullable=False)

class AppointmentRecords(db.Model):
    appointmentId = db.Column(db.Integer, nullable=False, primary_key=True)
    appointmentDate = db.Column(db.Date, nullable=False)
    appointmentStartTime = db.Column(db.TIMESTAMP, nullable=False)
    appointmentEndTime = db.Column(db.TIMESTAMP, nullable=False)
    appointmentTopic = db.Column(db.String(50), nullable=False)
    appointmentComment = db.Column(db.String(200))
    facultyId = db.Column(db.Integer, ForeignKey(Faculties.facultyId), nullable=False)
    studentId = db.Column(db.Integer, nullable=True)
    studentEmail = db.Column(db.String(50), nullable=False)
    majorId = db.Column(db.Integer, ForeignKey(Majors.majorId))
    departmentId = db.Column(db.Integer, ForeignKey(Departments.departmentId))

class TicketRecords(db.Model):
    ticketId = db.Column(db.Integer, nullable=False, primary_key=True)
    studentId = db.Column(db.Date, nullable=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    ticketTitle = db.Column(db.String(100))
    ticketContent = db.Column(db.String(100))
    solved = db.Column(db.BOOLEAN, nullable=False)
    advisorId = db.Column(db.Integer, ForeignKey(Faculties.facultyId))
    studentEmail = db.Column(db.String(50), nullable=False)
    departmentId = db.Column(db.Integer, ForeignKey(Departments.departmentId))
    majorId = db.Column(db.Integer, ForeignKey(Majors.majorId))




