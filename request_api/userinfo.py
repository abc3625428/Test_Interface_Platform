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

        #         # con = c.session()
        #         # res  = con.query(User).fliter_by(user_id=id).first()
        #         #
        #         # user_data = {}
        #         # # user_data['user_id'] = user.id
        #         # user_data['user_name'] = res.user_name
        #         # user_data['user_avatar'] = res.avatar
        #         # user_data['user_time'] =  res.modification_time
        #         # user_data['ruleNames'] = 111
        #         #
        #         # menus_id = res.menus_id
        #         # menus_data = con.query(Menus).fliter_by(menus_id=menus_id)
        #         # user_data['menus'] = menus_data.master
        #         #
        #         # logger.info('数据取回结果信息:{}'.format(user_data))
        #         # current_app.logger.info('current,app info')
        #         # write_trace_log("write_trace_log",read_time= datetime.datetime.now())

        result = {"user_time":20240311,
                  "user_name":"御弟哥哥",
                  "user_avatar":"url",
                  "1":"1",
                  "ruleNames":[111],
                  "menus":[{
                    "name": "后台管理",
                    "icon": "help",
                    "child": [{
                            "name": "主控台",
                            "icon": "home-filled",
                            "frontpath": "/"
                        }, {
                            "name": "用户中心",
                            "icon": "home-filled",
                            "frontpath": "/userCentre"
                        },
                        {
                            "name": "数据中心",
                            "icon": "home-filled",
                            "frontpath": "/dataCentre"
                        }, {
                            "name": "物料中心",
                            "icon": "home-filled",
                            "frontpath": "/materialCentre"
                        }
                    ]
                    }, {
                    "name": "Interface",
                    "icon": "help",
                    "child": [{
                        "name": "测试总览",
                        "icon": "shopping-bag",
                        "frontpath": "/interface"
                    }, {
                        "name": "测试结果统计",
                        "icon": "shopping-bag",
                        "frontpath": "/interface/result"
                    }, {
                        "name": "测试用例管理",
                        "icon": "shopping-bag",
                        "frontpath": "/interface/case"
                    }, {
                        "name": "数据大盘展示",
                        "icon": "shopping-bag",
                        "frontpath": "/interface/resultlist"
                    }]
                    }, {
                    "name": "策略测试",
                    "icon": "help",
                    "child": [{
                        "name": "测试总览",
                        "icon": "shopping-bag",
                        "frontpath": "/stratagem"
                    }, {
                        "name": "测试结果统计",
                        "icon": "shopping-bag",
                        "frontpath": "/stratagem/result"
                    }, {
                        "name": "数据召回",
                        "icon": "shopping-bag",
                        "frontpath": "/stratagem/recall"
                    }, {
                        "name": "测试用例管理",
                        "icon": "shopping-bag",
                        "frontpath": "/stratagem/case"
                    }, {
                        "name": "数据大盘展示",
                        "icon": "shopping-bag",
                        "frontpath": "/stratagem/resultlist"
                    }]
                    }, {
                    "name": "性能测试",
                    "icon": "help",
                    "child": [{
                        "name": "测试总览",
                        "icon": "shopping-bag",
                        "frontpath": "/performance"
                    }, {
                        "name": "测试结果统计",
                        "icon": "shopping-bag",
                        "frontpath": "/performance/result"
                    }, {
                        "name": "线上流量录制",
                        "icon": "shopping-bag",
                        "frontpath": "/performance/flowrecording"
                    }, {
                        "name": "测试用例管理",
                        "icon": "shopping-bag",
                        "frontpath": "/performance/case"
                    }, {
                        "name": "数据大盘展示",
                        "icon": "shopping-bag",
                        "frontpath": "/performance/resultlist"
                    }]
                    }, {
                    "name": "系统设置",
                    "icon": "help",
                    "child": [{
                        "name": "UI设置",
                        "icon": "home-filled",
                        "frontpath": "/set/ui"
                    }, {
                        "name": "公告",
                        "icon": "home-filled",
                        "frontpath": "/set/show"
                    }]
                    }]
                                  }

        return result,200

