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

class USER_USERINFO(Resource):


    def post(self):

        # data = request.get_json()
        #
        # print(data)
        #
        # username = data.get('username')
        # password = data.get('password')

            result = {"user_time":20240311,
                      "user_name":"御弟哥哥",
                      "user_avatar":"url",
                      "1":"1",
                      "ruleNames":[{1:1},{2:2}],
                      "menus":[{"name":"后台管理","icon":"help","child":[{"name":"主控台","icon":"home-filled","frontpath":"/"},{"name":"数据中心","icon":"home-filled","frontpath":"/dataCentre"},{"name":"用户中心","icon":"home-filled","frontpath":"/userCentre"},{"name":"物料中心","icon":"home-filled","frontpath":"/materialCentre"}]},{"name":"Interface","icon":"help","child":[{"name":"测试总览","icon":"shopping-bag","frontpath":"/interface"},{"name":"测试结果统计","icon":"shopping-bag","frontpath":"/interface/result"},{"name":"测试用例管理","icon":"shopping-bag","frontpath":"/interface/case"},{"name":"数据大盘展示","icon":"shopping-bag","frontpath":"/interface/resultlist"}]},{"name":"策略测试","icon":"help","child":[{"name":"测试总览","icon":"shopping-bag","frontpath":"/stratagem"},{"name":"测试结果统计","icon":"shopping-bag","frontpath":"/stratagem/result"},{"name":"数据召回","icon":"shopping-bag","frontpath":"/stratagem/recall"},{"name":"测试用例管理","icon":"shopping-bag","frontpath":"/stratagem/case"},{"name":"数据大盘展示","icon":"shopping-bag","frontpath":"/stratagem/resultlist"}]},{"name":"性能测试","icon":"help","child":[{"name":"测试总览","icon":"shopping-bag","frontpath":"/performance"},{"name":"测试结果统计","icon":"shopping-bag","frontpath":"/performance/result"},{"name":"线上流量录制","icon":"shopping-bag","frontpath":"/performance/flowrecording"},{"name":"测试用例管理","icon":"shopping-bag","frontpath":"/performance/case"},{"name":"数据大盘展示","icon":"shopping-bag","frontpath":"/performance/resultlist"}]},{"name":"系统设置","icon":"help","child":[{"name":"UI设置","icon":"home-filled","frontpath":"/set/ui"},{"name":"公告","icon":"home-filled","frontpath":"/set/show"}]}]
                      }
            return result,200

    def get(self):

        result = {"user": "wky","user_time":20240311}
        return result,200