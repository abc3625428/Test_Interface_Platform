from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime

from log import write_trace_log
from models.user import db,User,Role
from models import RoutingSqlAlchemy
import parser
from flask import current_app

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class USER_ROLE(Resource):

    def get(self):

        con = c.session()
        query = con.query(Role).order_by(Role.id.desc())
        count = con.query(Role).count()
        res = con.query(Role)
        result = []

        for element in res:

            role_data = {}
            role_data['id'] = element.id
            role_data['name'] = element.name


            result.append(role_data)

        logger.info('role取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log", read_time=datetime.datetime.now())

        data = {}
        data['roles'] = result

        return data, 200

    def post(self):

        params = request.get_json()

        if params.get('name') is None:
            return '请检查参数', 405

        print(params)
        name = params.get('name')

        con = c.session()
        u = con.query(Role).order_by(Role.id.desc()).first()
        if u != None:
            id = int(u.id)+1
        else:
            id = 1
        try:
            user_add = Role(name=name,id=id)
            con.add(user_add)
            con.commit()

            return 'role添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加role失败，请检查参数', 400


