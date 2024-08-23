from flask import Blueprint
from flask_restful import Api


from output import output_json
from . import question_all


# 响应结构处理
question_bp = Blueprint('question_bp', __name__)
question = Api(question_bp, catch_all_404s=True)
question.representation('application/json')(output_json)


# 问题列表 增删改查搜
question.add_resource(question_all.QUESTION_ADD,'/question/add',endpoint='question_add')
question.add_resource(question_all.QUESTION_DELETE,'/question/delete',endpoint='question_delete')
question.add_resource(question_all.QUESTION_MODIFY,'/question/modify',endpoint='question_modify')
question.add_resource(question_all.QUESTIONLISTGETDATA,'/question/add',endpoint='question_getdata')
question.add_resource(question_all.QUESTIONSEARCH,'/question/add',endpoint='question_search')
