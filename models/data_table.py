from models import db

# BigModelReport
class BigModelReport(db.Model):

    __tablename__ = 'bigmodeldata'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deta = db.Column(db.String(45))
    dataset = db.Column(db.String(45))
    version = db.Column(db.String(45))
    metric = db.Column(db.String(100))
    mode = db.Column(db.String(45))
    vllm = db.Column(db.String(45))
    modelname = db.Column(db.String(45))
