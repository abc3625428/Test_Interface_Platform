from models import db

# AllQuestingReport
class AllQuestingReport(db.Model):

    __tablename__ = 'all_question_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_class = db.Column(db.Integer)
    question_level = db.Column(db.Integer)
    question_fd_person = db.Column(db.String(10))
    question_dw_person = db.Column(db.String(10))
    question_state = db.Column(db.Integer)
    question_model = db.Column(db.String(10))
    question_frequency = db.Column(db.Integer)
    question_explain = db.Column(db.String(100))
    question_fd_time = db.Column(db.String(45))
    question_dw_time = db.Column(db.String(45))
    question_port = db.Column(db.String(45))
    question_demand = db.Column(db.String(45))


