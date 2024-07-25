

from models import db

import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index,BigInteger



# 用户数据表
class Schedule(db.Model):

    __tablename__ = 'schedule_task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    func = db.Column(db.String(50))
    args = db.Column(db.Integer)
    trigger = db.Column(db.String(50))
    month = db.Column(db.Integer)
    day = db.Column(db.String(50))
    hour = db.Column(db.String(50))
    minute = db.Column(db.String(50))
    second = db.Column(db.String(50))