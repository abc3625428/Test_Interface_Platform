from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from log import write_trace_log
import log
import datetime
from models.pickture import db,PICKTURE
from models import RoutingSqlAlchemy

from flask import current_app


logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

# class GETEMAGELISTPICK(Resource):
#
#
#     def get(self,currentPage,classpage):
#
#
#         result = {
#
#             "list":[
#                 {"id": "1","image_count": 14,"name": "人物", "url": "https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "人物", "url": "https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "人物", "url": "https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "人物", "url": "https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "人物", "url": "https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "高级", "url": "http://gips2.baidu.com/it/u=195724436,3554684702&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "严重问题", "url": "http://gips0.baidu.com/it/u=828570294,3060139577&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "优先处理问题", "url": "http://gips0.baidu.com/it/u=1674525583,3037683813&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "优先处理问题", "url": "http://gips2.baidu.com/it/u=195724436,3554684702&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "优先处理问题", "url": "http://gips2.baidu.com/it/u=4248708052,2809939788&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "优先处理问题", "url": "http://gips2.baidu.com/it/u=4248708052,2809939788&fm=3028"},
#                 {"id": "1", "image_count": 14, "name": "优先处理问题", "url": "http://gips2.baidu.com/it/u=4248708052,2809939788&fm=3028"},
#             ],
#             "totalCount":30
#
#         }
#         return result,200


class GETEMAGELISTPICK(Resource):


    def get(self,currentPage,classpage):



        page = int(currentPage)
        per_page = 12



        print(page,per_page)

        con = c.session()

        l = con.query(PICKTURE).filter_by(class_id = classpage).count()
        offset_data = (page - 1) * per_page
        res = con.query(PICKTURE).filter_by(class_id = classpage).offset(offset_data).limit(per_page)
        result = []

        for element in res:

            element_data = {}

            element_data['id'] = element.id
            element_data['image_count'] = element.class_id
            element_data['name'] =  element.pickture_name
            element_data['url'] = element.url
            result.append(element_data)
        logger.info('数据取回结果信息:{}'.format(result))
        current_app.logger.info('current,app info')
        write_trace_log("write_trace_log",read_time= datetime.datetime.now())
        data = {}
        data['list'] = result
        data['totalCount'] = l
        data['pageNum'] = page

        return data,200

class ADDEMAGELI(Resource):

    def post(self):

        params = request.get_json()

        if params.get('image_class_id') is None or params.get('img') is None:
            return '请检查参数', 405

        print(params)


        image_class_id = params.get('image_class_id')
        img = params.get('img')


        modification_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")



        con = c.session()
        u = con.query(PICKTURE).order_by(PICKTURE.id.desc()).first()
        if u != None:
            info_id = user_id = int(u.id)+1
        else:
            info_id = user_id = 1
        try:
            pickture_add = PICKTURE(pickture_class_name='Pickture',class_id=image_class_id,id=user_id,url=img,time=modification_time)
            con.add(pickture_add)
            con.commit()

            return '添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加失败，请检查参数', 400
