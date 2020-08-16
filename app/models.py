from app import db
from sqlalchemy import Binary, Table, Column, Integer, ForeignKey

class roles(db.Model):
    roleId = db.Column(db.Integer, nullable=False, primary_key=True)
    roleName = db.Column(db.String(), nullable=False)

class facultys(db.Model):
    facultyId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.Binary(64))
    salt = db.Column(db.Binary(64))
    roleId = db.Column(db.Integer, ForeignKey(roles.roleId))
