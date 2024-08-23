from flask import Blueprint
from flask_restful import Api


from output import output_json
from . import newperson


# 响应结构处理
data_bp = Blueprint('data_bp', __name__)
data = Api(data_bp, catch_all_404s=True)
data.representation('application/json')(output_json)


# da模型数据
data.add_resource(newperson.GETBIGMODEL_LISTDATA,'/admin/data/bigmodellist',endpoint='bigmodellist')
data.add_resource(newperson.NEWPERSON_DATA,'/admin/data/bigmodel/<path:model>',endpoint='newperson')
data.add_resource(newperson.NEWPERSON_ADD,'/admin/data/addnewperson',endpoint='addnewperson')
