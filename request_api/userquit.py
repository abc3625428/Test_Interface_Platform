from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log

from models.user import db,UserAccountData
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class USER_QUIT(Resource):


    def post(self):

            result = "用户已退出"
            return result,200

    def get(self):

        result = {"user": "wky","user_time":20240311}
        return result,200