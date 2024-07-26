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

class GETSTATISTICS2(Resource):

    def get(self):


        result = {

            "goods":[
            {"label": "Interface","value": 140},
            {"label": "策略问题", "value": 30},
            {"label": "性能问题", "value": 50},
            {"label": "全部问题", "value": 60}
            ],

            "order":[
            {"label": "总错误", "value": 140},
            {"label": "特殊问题", "value": 30},
            {"label": "严重问题", "value": 50},
            {"label": "一般问题", "value": 60}
            ]

        }
        return result,200