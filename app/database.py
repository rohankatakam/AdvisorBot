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
    return dep.departmentid


def add_major(majorname, departmentid):
    major = Majors(majorname=majorname, departmentid=departmentid)
    db.session.add(major)
    db.session.commit()
    return major.majorid


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
    return record.appointmentid


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
                      time=datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    db.session.add(t)
    db.session.commit()
    return t.ticketid


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

# Date is string formatted as YYYY-MM-DD
# Output time is formatted as YYYY-MM-DD HH:MM:SS
def find_appointment_slots(departmentid, date):
    appointments = AppointmentRecords.query.join(
        AppointmentRecords.departmentid == departmentid,
        AppointmentRecords.appointmentdate == date).order_by(Faculties.username.asc())

    faculties = Faculties.query.order_by(Faculties.username.asc()).all()
    slots = {}
    for f in faculties:
        a = []
        for i in range(0, 8 * 2):
            time = date + "{:02d}:{:02d}:00".format(9 + int(i/2), int(i % 2)*30)
            a.append(time)
        slots[f.username] = a