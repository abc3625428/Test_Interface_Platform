from models import db

import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index,BigInteger



# PICKTURECLASS
class PICKTURECLASS(db.Model):

    __tablename__ = 'pickture_class'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))
    pickture_classcol = db.Column(db.Integer)
    time = db.Column(db.DateTime)


class PICKTURE(db.Model):

    __tablename__ = 'pickture'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pickture_class_name = db.Column(db.String(45))
    class_id = db.Column(db.Integer)
    url = db.Column(db.String(100))
    pickture_name = db.Column(db.String(45))
    time = db.Column(db.DateTime)
    image = db.Column(db.LargeBinary)
