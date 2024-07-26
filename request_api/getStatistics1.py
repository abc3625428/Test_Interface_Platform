from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime


from log import write_trace_log
from models.user import db,UserAccountData,User,Menus
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETSTATISTICS1(Resource):



    def get(self):


        result = {"panels":[

            {"subTitle": "总执行次数", "subUnit": "1", "subValue": 1024, "title": "执行次数", "unit": "月", "unitColor": "success","value": 140},
            {"subTitle": "执行失败率", "subUnit": "2", "subValue": "10%", "title": "interface自动化", "unit": "月", "unitColor": "success","value": 30},
            {"subTitle": "执行失败率", "subUnit": "3", "subValue": "2%", "title": "策略自动化", "unit": "月", "unitColor": "success","value": 50},
            {"subTitle": "执行失败率", "subUnit": "4", "subValue": "4%", "title": "性能测试", "unit": "月", "unitColor": "success","value": 60}
    ]}
        return result,200