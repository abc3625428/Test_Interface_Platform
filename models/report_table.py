from models import db

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


# AllAutoReport
class AllAutoReport(db.Model):

    __tablename__ = 'all_auto_result'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_class = db.Column(db.Integer)
    result = db.Column(db.String(10))
    name = db.Column(db.String(10))
    all_result = db.Column(db.Integer)
    pass_result = db.Column(db.Integer)


