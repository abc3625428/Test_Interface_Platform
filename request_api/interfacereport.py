from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime

from log import write_trace_log
from models.user import db,UserAccountData
from models.report_table import InterfaceAutoReport
from models import RoutingSqlAlchemy
import parser
from flask import current_app

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class REPORT_DATA_ADD(Resource):


    def post(self):

        params = request.get_json()

        if params.get('report_all') is None or params.get('report_pass') is None or params.get('report_fail') is None or params.get('report_skip') is None:
            return '请检查参数', 405

        print(params)
        report_all = params.get('report_all')
        report_pass = params.get('report_pass')
        report_fail = params.get('report_fail')
        report_skip = params.get('report_skip')
        report_error = params.get('report_error')
        report_failure = params.get('report_failure')
        report_url = params.get('report_url')
        report_execution_time = params.get('report_execution_time')
        interface_auto_reportcol = params.get('interface_auto_reportcol')
        report_name = params.get('report_name')


        con = c.session()
        u = con.query(InterfaceAutoReport).order_by(InterfaceAutoReport.id.desc()).first()
        report_id = int(u.report_id)+1
        id = int(u.id) + 1

        try:
            user_add = InterfaceAutoReport(id=id,report_id=report_id,report_all=report_all,report_pass=report_pass,report_fail=report_fail,
                                           report_skip=report_skip,report_error=report_error,report_failure=report_failure,
                                           report_url=report_url,report_execution_time=report_execution_time,report_name=report_name,
                                           interface_auto_reportcol=interface_auto_reportcol)

            con.add(user_add)
            con.commit()

            return '报告添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加报告失败，请检查参数', 400


class REPORT_DATA_DELETE(Resource):

    def post(self,id):

        params = request.get_json()
        con = c.session()
        try:
            con.query(InterfaceAutoReport).filter(InterfaceAutoReport.id == id).delete()
            con.commit()

        except IOError as E:
            return E,500

        return '用户删除成功',200


class REPORT_DATA_UPDATE(Resource):

    def post(self):

        params = request.get_json()

        if params.get('mobile') is None or params.get('user_name') is None or params.get('account') is None or params.get('email') is None:
            return [{'code':-1},{'error':'请检查参数'}], 405

        print(params)
        mobile = str(params.get('mobile'))
        user_name = params.get('user_name')
        email = params.get('email')
        account = str(params.get('account'))
        # user_id = data.get('user_id')

        con = c.session()

        try:
            con.query(InterfaceAutoReport).filter(InterfaceAutoReport.account == account).update({InterfaceAutoReport.phone:mobile, InterfaceAutoReport.user_name:user_name, InterfaceAutoReport.email:email, InterfaceAutoReport.account:account})
            con.commit()

        except IOError as E:
            return E,500

        return '用户信息修改成功',200



class REPORT_DATA_TABLE(Resource):

    def get(self,currentPage):


        if currentPage is None:
            page = 1
            per_page = 10
        else:
            page = int(currentPage)
            per_page = 10


        print(page,per_page)

        con = c.session()
        query = con.query(InterfaceAutoReport).order_by(InterfaceAutoReport.id.desc())
        l = con.query(InterfaceAutoReport).count()
        # results = query.paginate(page=page, per_page=per_page, error_out=False, max_per_page=50).itmes
        offset_data = (page - 1) * per_page
        res = con.query(InterfaceAutoReport).offset(offset_data).limit(per_page)
        result = []

        for report in res:

            report_data = {}
            report_data['id'] = report.id
            report_data['report_all'] = report.report_all
            report_data['report_pass'] = report.report_pass
            report_data['report_fail'] = report.report_fail
            report_data['report_skip'] = report.report_skip
            report_data['report_error'] = str(report.report_error)
            report_data['report_failure'] = report.report_failure
            report_data['report_url'] = report.report_url
            report_data['interface_auto_reportcol'] = report.interface_auto_reportcol
            report_data['report_name'] = report.report_name
            report_data['report_execution_time'] = report.report_execution_time

            result.append(report_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log", read_time=datetime.datetime.now())
        data = {}
        data['list'] = result
        data['totalCount'] = l
        data['pageNum'] = page

        return data, 200


    def post(self):

        params = request.get_json()
        print(params)

        if params.get('currentPage') == None or params.get('pageSize') == None:
            page = 1
            per_page = 10
        else:
            page = int(params.get('currentPage'))
            per_page = int(params.get('pageSize'))

        print(page, per_page)

        con = c.session()
        query = con.query(InterfaceAutoReport).order_by(InterfaceAutoReport.id.desc())
        l = con.query(InterfaceAutoReport).count()
        # results = query.paginate(page=page, per_page=per_page, error_out=False, max_per_page=50).itmes
        offset_data = (page - 1) * per_page
        res = con.query(InterfaceAutoReport).offset(offset_data).limit(per_page)
        result = []

        for report in res:

            report_data = {}
            report_data['id'] = report.id
            report_data['report_all'] = report.report_all
            report_data['report_pass'] = report.report_pass
            report_data['report_fail'] = report.report_fail
            report_data['report_skip'] = report.report_skip
            report_data['report_error'] = str(report.report_error)
            report_data['report_skip'] = report.report_skip
            report_data['report_failure'] = report.report_failure
            report_data['report_url'] = report.report_url
            report_data['interface_auto_reportcol'] = report.interface_auto_reportcol
            report_data['report_name'] = report.report_name
            report_data['report_execution_time'] = report.report_execution_time

            result.append(report_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log", read_time=datetime.datetime.now())
        data = {}
        data['list'] = result
        data['total'] = l
        data['pageNum'] = page

        return data, 200