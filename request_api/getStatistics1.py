from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime


from log import write_trace_log
from models.report_table import AllAutoReport
from models import RoutingSqlAlchemy
from flask import current_app

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETSTATISTICS1(Resource):



    def get(self):


        con = c.session()

        report_cont = con.query(AllAutoReport).count()
        pass_cont = con.query(AllAutoReport).filter_by(result=1).count()
        value = pass_cont // report_cont


        report_all = con.query(AllAutoReport).all()


        success_ = (str(int(value * 100))+"%")

        res = []

        for element in report_all:

            element_data = {}
            element_data['user_id'] = element.id
            element_data['report_class'] = element.report_class
            element_data['result'] = element.result
            element_data['all_result'] =  element.all_result
            element_data['pass_result'] = element.pass_result
            res.append(element_data)
        print(res)

        logger.info('数据取回结果信息:{}'.format(res))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log",read_time= datetime.datetime.now())




        result = {"panels":[

            {"subTitle": "总执行成功率", "subUnit": "1", "subValue": success_, "title": "总执行次数", "unit": "测试", "unitColor": "success","value": report_cont},
            {"subTitle": "执行成功率", "subUnit": "2", "subValue": success_, "title": "interface自动化", "unit": "测试", "unitColor": "success","value": report_cont},
            {"subTitle": "执行成功率", "subUnit": "3", "subValue": success_, "title": "策略自动化", "unit": "测试", "unitColor": "success","value": report_cont},
            {"subTitle": "执行成功率", "subUnit": "4", "subValue": success_, "title": "性能测试", "unit": "测试", "unitColor": "success","value": report_cont}
    ]}
        return result,200