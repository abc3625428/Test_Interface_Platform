from models import db

# InterfaceAutoCase
class InterfaceAutoCase(db.Model):

    __tablename__ = 'interfacecase_aig'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer)
    case_id = db.Column(db.Integer)
    case_mode = db.Column(db.String(45))
    case_name = db.Column(db.String(45))
    case_url = db.Column(db.String(200))
    request_mode = db.Column(db.String(45))
    request_type = db.Column(db.String(45))
    request_parameter = db.Column(db.String(5000))
    request_head = db.Column(db.String(5000))
    target_key = db.Column(db.String(45))
    is_valid = db.Column(db.Integer)
    is_execute = db.Column(db.Integer)
    precondition = db.Column(db.String(45))
    status_code = db.Column(db.String(45))
    expected_result = db.Column(db.String(45))
    modification_time = db.Column(db.String(45))
    interfacecase_user = db.Column(db.String(45))


# InterfaceAutoClass
class InterfaceAutoClass(db.Model):

    __tablename__ = 'interfacecase_class'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    interface_classcol = db.Column(db.String(45))
    time = db.Column(db.String(45))

