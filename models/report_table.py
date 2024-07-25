from models import db

import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index,BigInteger



# InterfaceAutoReport
class InterfaceAutoReport(db.Model):

    __tablename__ = 'interface_auto_report'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_id = db.Column(db.Integer, primary_key=True)
    report_all = db.Column(db.String(10))
    report_pass = db.Column(db.String(10))
    report_fail = db.Column(db.String(10))
    report_skip = db.Column(db.String(10))
    report_error = db.Column(db.String(10))
    report_failure = db.Column(db.String(10))
    report_url = db.Column(db.String(100))
    report_execution_time = db.Column(db.String(45))
    interface_auto_reportcol = db.Column(db.String(45))
    report_name = db.Column(db.String(45))
