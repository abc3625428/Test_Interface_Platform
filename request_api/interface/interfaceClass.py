from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from log import write_trace_log
import log
import datetime
from models.interface import InterfaceAutoClass
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETINTERFACELIST(Resource):


    def get(self,currentPage):



        page = int(currentPage)
        per_page = 10



        print(page,per_page)

        con = c.session()

        l = con.query(InterfaceAutoClass).count()
        offset_data = (page - 1) * per_page
        res = con.query(InterfaceAutoClass).offset(offset_data).limit(per_page)
        result = []

        for user in res:

            user_data = {}

            user_data['id'] = user.id
            user_data['name'] = user.name
            user_data['image_count'] =  user.interface_classcol
            user_data['order'] = user.interface_classcol
            result.append(user_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log",read_time= datetime.datetime.now())
        data = {}
        data['list'] = result
        data['totalCount'] = l
        data['pageNum'] = page

        return data,200


class ADDINTERFACELIST(Resource):

    def post(self):

        params = request.get_json()

        if params.get('name') is None or params.get('order') is None:
            return '请检查参数', 405

        print(params)


        name = params.get('name')
        order = params.get('order')


        modification_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



        con = c.session()
        u = con.query(InterfaceAutoClass).order_by(InterfaceAutoClass.id.desc()).first()
        if u != None:
            info_id = user_id = int(u.id)+1
        else:
            info_id = user_id = 1
        try:
            add = InterfaceAutoClass(name=name,id=user_id,pickture_classcol=order,time=modification_time)
            con.add(add)
            con.commit()

            return '添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加失败，请检查参数', 400



class INTERFACECLASS_DELETE(Resource):

    def post(self, id):

        con = c.session()
        try:
            con.query(InterfaceAutoClass).filter(InterfaceAutoClass.id == id).delete()
            con.commit()

        except IOError as E:
            return E, 500

        return '删除成功', 200