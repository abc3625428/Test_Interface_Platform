from flask import request
from flask_restful import Resource
from sqlalchemy.sql import func

import log
import datetime

from models.data_table import BigModelReport
from models import RoutingSqlAlchemy

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETBIGMODEL_LISTDATA(Resource):

    def get(self):

        con = c.session()
        r = con.query(BigModelReport.modelname).group_by(BigModelReport.modelname).all()

        result = []


        for element in r:
            di = {}

            di['label'] = element.modelname
            di['value'] = element.modelname
            result.append(di)


        return result, 200



class NEWPERSON_DATA(Resource):

    def get(self, model):

        con = c.session()
        r = con.query(BigModelReport).filter(BigModelReport.modelname==model).all()

        # results = con.query(BigModelReport.vllm).group_by(BigModelReport.metric).all()

        ls_se = []
        ls_set = []
        ls_p_recall = []
        ls_p_precision = []

        di_p_recall = {}
        di_p_precision = {}


        for element in r:

            if element.metric == 'p_recall':
                di_p_recall[element.dataset] = element.vllm
                ls_p_recall.append(element.vllm)

            if element.metric == 'p_precision':
                di_p_precision[element.dataset] = element.vllm
                ls_p_precision.append(element.vllm)
                ls_se.append(element.dataset[6:])

        for i in ls_se:
            if 'experience' in i:
                ls_set.append(i[11:])
            else:
                ls_set.append(i)


        option = {
            "title": {
                "text": ["qwen1.5-14b-chat-vllm"]
            },
            "tooltip": {
                "trigger": 'axis'
            },
            "legend": {
                "data": ['p_recall', 'p_precision']
            },
            "grid": {
                "left": '3%',
                "right": '4%',
                "bottom": '3%',
                "containLabel": True
            },
            "toolbox": {
                "feature": {
                    "saveAsImage": {}
                }
            },
            "xAxis": {
                "type": 'category',
                "boundaryGap": False,
                "data": ls_set
            },
            "yAxis": {
                "type": 'value'
            },
            "series": [
                {
                    "name": 'p_recall',
                    "type": 'line',
                    "stack": 'Total',
                    "data": ls_p_recall
                },
                {
                    "name": 'p_precision',
                    "type": 'line',
                    "stack": 'Total',
                    "data": ls_p_precision
                }

            ]
        }

        return option, 200


class NEWPERSON_ADD(Resource):

    def post(self):

        params = request.get_json()
        if params.get('dataset') is None or params.get('version') is None or params.get('metric') is None or params.get('mode') is None:
            return '请检查参数', 405

        print(params)

        dataset = params.get('dataset')
        version = params.get('version')
        metric = params.get('metric')
        mode = params.get('mode')
        vllm = params.get('vllm')
        modelname = params.get('modelname')
        deta =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")



        con = c.session()

        u = con.query(BigModelReport).order_by(BigModelReport.id.desc()).first()
        if u != None:
            info_id = int(u.id)+1
        else:
            info_id = 1
        try:
            BigModelReport_add = BigModelReport(dataset=dataset,id=info_id,version=version,metric=metric,mode=mode,
                                vllm=vllm,modelname=modelname,deta=deta)
            con.add(BigModelReport_add)
            con.commit()

            return '模型数据添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加模型数据失败，请检查参数', 400