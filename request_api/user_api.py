from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime

from log import write_trace_log
from models.user import db,User
from models import RoutingSqlAlchemy
import parser
from flask import current_app

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class USER_DATA_ADD(Resource):


    def post(self):

        params = request.get_json()

        if params.get('mobile') is None or params.get('user_name') is None or params.get('account') is None or params.get('email') is None:
            return '请检查参数', 405

        print(params)
        mobile = params.get('mobile')
        user_name = params.get('user_name')
        email = params.get('email')

        # user_id = data.get('user_id')


        con = c.session()
        u = con.query(User).order_by(User.user_id.desc()).first()
        user_id = int(u.user_id)+1
        try:
            user_add = User(phone=mobile,user_name=user_name,email=email,user_id=user_id)
            con.add(user_add)
            con.commit()

            return '用户添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加用户失败，请检查参数', 400


class USER_DATA_DELETE(Resource):

    def post(self):

        params = request.get_json()

        if  params.get('account') is None:
            return {'error':'请检查参数'}, 405

        print(params)
        # mobile = str(params.get('mobile'))
        # user_name = params.get('user_name')
        # email = params.get('email')
        account = str(params.get('account'))
        # user_id = data.get('user_id')

        con = c.session()

        try:
            con.query(User).filter(User.account == account).delete()
            con.commit()

        except IOError as E:
            return E,500

        return '用户删除成功',200


class USER_DATA_UPDATE(Resource):

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
            con.query(User).filter(User.account == account).update({User.phone:mobile, User.user_name:user_name, User.email:email, User.account:account})
            con.commit()

        except IOError as E:
            return E,500

        return '用户信息修改成功',200



class USER_DATA_TABLE(Resource):

    def get(self):


        if request.args.get('currentPage') is None or request.args.get('pageSize') is None:
            page = 1
            per_page = 8
        else:
            page = int(request.args.get('currentPage'))
            per_page = int(request.args.get('pageSize'))


        print(page,per_page)

        con = c.session()
        query  = con.query(User).order_by(User.id.desc())
        l = con.query(User).count()
        # results = query.paginate(page=page, per_page=per_page, error_out=False, max_per_page=50).itmes
        offset_data = (page - 1) * per_page
        res = con.query(User).offset(offset_data).limit(per_page)
        result = []

        for user in res:

            user_data = {}
            # user_data['user_id'] = user.user_id
            user_data['account'] = user.account
            user_data['phone'] = user.phone
            user_data['email'] =  user.email
            user_data['user_name'] = user.user_name
            result.append(user_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log",read_time= datetime.datetime.now())
        data = {}
        data['list'] = result
        data['total'] = l
        data['pageNum'] = page

        return data,200


    def post(self):

        params = request.get_json()
        print(params)

        if params.get('currentPage') == None or params.get('pageSize') == None:
            page = 1
            per_page = 8
        else:
            page = int(params.get('currentPage'))
            per_page = int(params.get('pageSize'))

        print(page, per_page)

        con = c.session()
        query = con.query(User).order_by(User.id.desc())
        l = con.query(User).count()
        # results = query.paginate(page=page, per_page=per_page, error_out=False, max_per_page=50).itmes
        offset_data = (page - 1) * per_page
        res = con.query(User).offset(offset_data).limit(per_page)
        result = []

        for user in res:

            user_data = {}
            # user_data['user_id'] = user.user_id
            user_data['account'] = user.account
            user_data['phone'] = user.phone
            user_data['email'] = user.email
            user_data['user_name'] = user.user_name
            user_data['create_time'] = str(user.create_time)
            result.append(user_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log", read_time=datetime.datetime.now())
        data = {}
        data['list'] = result
        data['total'] = l
        data['pageNum'] = page

        return data, 200
