import hashlib
import os
import time
import datetime
from flask import current_app
from app.models import *
from flask_sqlalchemy import SQLAlchemy


def generate_password_hash(password, salt):
    return hashlib.sha512(password.encode('utf-8') + salt).digest()


def add_faculty(username, email, password, firstname, lastname):
    salt = os.urandom(64)
    password_hash = generate_password_hash(password, salt)
    faculty = Faculties(username=username, email=email,
                        password=password_hash, salt=salt,
                        firstname=firstname, lastname=lastname)
    db.session.add(faculty)
    db.session.flush()
    id = faculty.facultyid
    db.session.commit()
    return id


def add_department_record(facultyid, departmentid):
    record = DepartmentRecords(facultyid=facultyid, departmentid=departmentid)
    db.session.add(record)
    db.session.commit()


def add_department(departmentname):
    dep = Departments(departmentname=departmentname)
    db.session.add(dep)
    db.session.flush()
    id = dep.departmentid
    db.session.commit()
    return id


def add_major(majorname, departmentid):
    major = Majors(majorname=majorname, departmentid=departmentid)
    db.session.add(major)
    db.session.flush()
    id = major.majorid
    db.session.commit()
    return id


def add_appointment(studentemail,
                    facultyid,
                    majorid,
                    departmentid,
                    appointmentdate,
                    appointmentstartTime,
                    appointmenttopic,
                    appointmentcomment,
                    studentfirstname,
                    studentlastname):
    record = AppointmentRecords(studentemail=studentemail,
                                facultyid=facultyid,
                                majorid=majorid,
                                departmentid=departmentid,
                                appointmentdate=appointmentdate,
                                appointmentstarttime=appointmentstartTime,
                                appointmenttopic=appointmenttopic,
                                appointmentcomment=appointmentcomment,
                                studentfirstname=studentfirstname,
                                studentlastname=studentlastname)
    db.session.add(record)
    db.session.flush()
    id = record.appointmentid
    db.session.commit()
    return id


def add_ticket(studentemail,
               majorid,
               advisorid,
               departmentid,
               tickettitle,
               ticketcontent,
               studentfirstname,
               studentlastname):
    t = TicketRecords(studentemail=studentemail,
                      majorid=majorid,
                      advisorid=advisorid,
                      departmentid=departmentid,
                      tickettitle=tickettitle,
                      ticketcontent=ticketcontent,
                      solved=False,
                      studentfirstname=studentfirstname,
                      studentlastname=studentlastname,
                      time=datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    db.session.add(t)
    db.session.flush()
    id = t.ticketid
    db.session.commit()
    return id


def find_faculty_by_id(facultyid):
    return Faculties.query.filter(Faculties.facultyid == facultyid).first()


def find_faculty_by_username(username):
    return Faculties.query.filter(Faculties.username == username).first()


def find_department_by_name(departmentname):
    return Departments.query.filter(Departments.departmentname == departmentname).first()


def find_department_by_id(departmentid):
    return Departments.query.filter(Departments.departmentid == departmentid).first()


def find_department_by_majorname(majorname):
    return db.session.query(Departments)\
        .join(Majors, Departments.departmentid == Majors.departmentid)\
        .filter(Majors.majorname == majorname)


def find_appointment_by_id(appointmentid):
    record = AppointmentRecords.query.filter(
        AppointmentRecords.appointmentid == appointmentid).first()
    return record


def find_appointment_by_faculty_id(appointmentid):
    record = AppointmentRecords.query.filter(
        AppointmentRecords.appointmentid == appointmentid).first()
    return record


def login(username, password):
    faculty = Faculties.query.filter(
        Faculties.username == username).with_entities(Faculties.salt).first()
    if faculty is None:
        return False
    password_hash = generate_password_hash(password, faculty.salt)
    result = Faculties.query.filter(Faculties.password == password_hash)
    return result is not None

# Date is string formatted as YYYY-MM-DD
# Output time is formatted as YYYY-MM-DD HH:MM:SS


def find_appointment_slots(departmentid, date):
    appointments = db.session.query(AppointmentRecords)\
        .join(Faculties)\
        .filter(AppointmentRecords.departmentid == departmentid)\
        .order_by(Faculties.username.asc())

    faculties = Faculties.query.order_by(Faculties.username.asc()).all()
    slots = {}
    for f in faculties:
        a = []
        for i in range(0, 8 * 2):
            time = date + \
                " {:02d}:{:02d}:00".format(9 + int(i/2), int(i % 2)*30)
            a.append(time)
        slots[f.facultyid] = a
    if appointments is not None:
        for appoint in appointments:
            a = slots[appoint.facultyid]
            for t in a:
                if t == appoint.appointmentdate + " " + appoint.appointmentstarttime:
                    a.remove(t)
    return slots
