from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from log import write_trace_log
import log
import datetime
from models.pickture import db,PICKTURE,PICKTURECLASS
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETEMAGELIST(Resource):


    def get(self,currentPage):



        page = int(currentPage)
        per_page = 10



        print(page,per_page)

        con = c.session()

        l = con.query(PICKTURECLASS).count()
        offset_data = (page - 1) * per_page
        res = con.query(PICKTURECLASS).offset(offset_data).limit(per_page)
        result = []

        for user in res:

            user_data = {}

            user_data['id'] = user.id
            user_data['name'] = user.name
            user_data['image_count'] =  user.pickture_classcol
            user_data['order'] = user.pickture_classcol
            result.append(user_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log",read_time= datetime.datetime.now())
        data = {}
        data['list'] = result
        data['totalCount'] = l
        data['pageNum'] = page

        return data,200


class ADDEMAGELIST(Resource):

    def post(self):

        params = request.get_json()

        if params.get('name') is None or params.get('order') is None:
            return '请检查参数', 405

        print(params)


        name = params.get('name')
        order = params.get('order')


        modification_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")



        con = c.session()
        u = con.query(PICKTURECLASS).order_by(PICKTURECLASS.id.desc()).first()
        if u != None:
            info_id = user_id = int(u.id)+1
        else:
            info_id = user_id = 1
        try:
            pickture_add = PICKTURECLASS(name=name,id=user_id,pickture_classcol=order,time=modification_time)
            con.add(pickture_add)
            con.commit()

            return '添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加失败，请检查参数', 400



class PICKTURELIST_DELETE(Resource):

    def post(self, id):

        con = c.session()
        try:
            con.query(PICKTURECLASS).filter(PICKTURECLASS.id == id).delete()
            con.commit()

        except IOError as E:
            return E, 500

        return '图库删除成功', 200