import hashlib
import os
import time
import datetime
from flask import current_app
from app.models import *
from flask_sqlalchemy import SQLAlchemy


def generate_password_hash(password, salt):
    return hashlib.sha512(password.encode('utf-8') + salt).digest()


def add_faculty(username, email, password):
    salt = os.urandom(64)
    password_hash = generate_password_hash(password, salt)
    faculty = Faculties(username=username, email=email,
                        password=password_hash, salt=salt)
    db.session.add(faculty)
    db.session.commit()
    return faculty.facultyid


def add_department_record(facultyid, departmentid):
    record = DepartmentRecords(facultyid=facultyid, departmentid=departmentid)
    db.session.add(record)
    db.session.commit()


def add_department(departmentname):
    dep = Departments(departmentname=departmentname)
    db.session.add(dep)
    db.session.commit()


def add_major(majorname):
    major = Majors(majorname=majorname)
    db.session.add(major)
    db.session.commit()


def add_appointment(studentemail,
                    facultyid,
                    majorid,
                    departmentid,
                    appointmentdate,
                    appointmentstartTime,
                    appointmenttopic,
                    appointmentcomment):
    record = AppointmentRecords(studentemail=studentemail,
                                facultyid=facultyid,
                                majorid=majorid,
                                departmentid=departmentid,
                                appointmentdate=appointmentdate,
                                appointmentstartTime=appointmentstartTime,
                                appointmenttopic=appointmenttopic,
                                appointmentcomment=appointmentcomment)
    db.session.add(record)
    db.session.commit()


def add_ticket(studentemail,
               majorid,
               advisorid,
               departmentid,
               tickettitle,
               ticketcontent):
    t = TicketRecords(studentemail=studentemail,
                      majorid=majorid,
                      advisorid=advisorid,
                      departmentid=departmentid,
                      tickettitle=tickettitle,
                      ticketcontent=ticketcontent,
                      solved=False,
                      time=int(time.time() * 1000.0))
    db.session.add(t)
    db.session.commit()


def find_appointment_by_id(appointmentid):
    record = AppointmentRecords.query.filter(
        AppointmentRecords.appointmentid == appointmentid).first
    return record


def login(username, password):
    faculty = Faculties.query.filter(
        Faculties.username == username).with_entities(Faculties.salt).first()
    if faculty is None:
        return False
    password_hash = generate_password_hash(password, faculty.salt)
    result = Faculties.query.filter(Faculties.password == password_hash)
    return result is not None


def find_faculty_by_id(facultyid):
    return Faculties.query.filter(Faculties.facultyid == facultyid).first()


def find_faculty(departmentid, date):
    pass
    # appointments = AppointmentRecords.query.join