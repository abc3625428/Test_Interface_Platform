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

class NOTICEGETSTATISTICS1(Resource):


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
                      "ruleNames":[111],
                      "menus":[{'name':"后台管理",'icon':"help",'child':[{'name':"主控台",'icon':"home-filled",'frontpath':"/",},{'name':"数据中心",'icon':"home-filled",'frontpath':"/",},{'name':"用户中心",'icon':"home-filled",'frontpath':"/",},{'name':"物料中心",'icon':"home-filled",'frontpath':"/",},],},{'name':"Interface",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/goods/list",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"策略测试",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据召回",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"性能测试",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"线上流量录制",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"系统设置",'icon':"help",'child':[{'name':"UI设置",'icon':"home-filled",'frontpath':"/",},{'name':"展示设置",'icon':"home-filled",'frontpath':"/",},],},]
                      }
            return result,200

    def get(self):


        result = {"list":[
            {"id": 1, "title": "周执行时间", "content": "nip", "order": 0, "create_time": "2022-06-06 14:40:11","update_time": "2022-06-06 14:40:11"},
            {"id": 2, "title": "班车时间", "content": "nip", "order": 0, "create_time": "2022-06-06 14:40:11","update_time": "2022-06-06 14:40:11"},
            {"id": 3, "title": "客户端发版时间", "content": "nip", "order": 0, "create_time": "2022-06-06 14:40:11","update_time": "2022-06-06 14:40:11"},
            {"id": 5, "title": "小程序提审时间", "content": "nip", "order": 0, "create_time": "2022-06-06 14:40:11","update_time": "2022-06-06 14:40:11"},
            {"id": 6, "title": "需求遗留", "content": "nip", "order": 0, "create_time": "2022-06-06 14:40:11","update_time": "2022-06-06 14:40:11"},
            ],
            'totalCount':20
        }
        return result,200

