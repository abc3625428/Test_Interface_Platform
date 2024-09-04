from flask import request
from flask_restful import Resource
import log
import datetime
import json

from models.interface import InterfaceAutoCase
from models import RoutingSqlAlchemy

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GEAINTERFACEDATA(Resource):

    def get(self,currentPage):

        if currentPage is None:
            page = 1
            per_page = 10
        else:
            page = int(currentPage)
            per_page = 10

        search_keyword =  request.args.get('keyword')
        print(search_keyword)
        con = c.session()
        r = ''
        rr = []
        totalCount = 1
        if search_keyword == None:

            offset_data = (page - 1) * per_page
            r = con.query(InterfaceAutoCase).offset(offset_data).limit(per_page)
            totalCount = con.query(InterfaceAutoCase).count()

        else:

            offset_data = (page - 1) * per_page
            totalCount = con.query(InterfaceAutoCase).filter(InterfaceAutoCase.case_name.like(f'%{search_keyword}%')).count()
            r = con.query(InterfaceAutoCase).filter(InterfaceAutoCase.case_name.like(f'%{search_keyword}%')).offset(offset_data).limit(per_page)

        for element in r:

            role_data = {}
            element_data = {}
            element_data['case_id'] = element.case_id
            element_data['class_id'] = element.class_id
            element_data['case_mode'] = element.case_mode
            element_data['case_name'] = element.case_name
            element_data['case_url'] = element.case_url
            element_data['request_mode'] = element.request_mode
            element_data['request_type'] = element.request_type
            element_data['request_parameter'] = element.request_parameter
            element_data['request_head'] = element.request_head
            element_data['target_key'] = element.target_key
            element_data['is_valid'] = element.is_valid
            element_data['is_execute'] = element.is_execute

            element_data['precondition'] = element.precondition
            element_data['status_code'] = element.status_code
            element_data['expected_result'] = element.expected_result
            element_data['modification_time'] = element.modification_time
            element_data['interfacecase_user'] = element.interfacecase_user

            # roledata = con.query(InterfaceAutoCase).filter(element.belonging_role==InterfaceAutoCase.id).first()
            # role_data['id'] = roledata.id
            # role_data['name'] = roledata.name
            # element_data['role'] = role_data

            rr.append(element_data)




        result = {}



        result['list'] = rr
        result['totalCount'] = totalCount

        logger.info('数据取回结果信息:{}'.format(result))

        return result,200


class INTERFACE_ADD(Resource):

    def post(self):

        params = request.get_json()

        if params.get('case_url') is None:
            return '请检查参数', 405

        print(params)

        class_id = params.get('class_id')
        case_mode = params.get('case_mode')
        case_name = params.get('case_name')
        case_url = params.get('case_url')
        request_mode = params.get('request_mode')
        request_type = params.get('request_type')
        request_parameter = params.get('request_parameter')
        request_head = params.get('request_head')
        target_key = params.get('target_key')

        modification_time =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        is_valid = params.get('is_valid')
        is_execute = params.get('is_execute')
        precondition = params.get('precondition')
        status_code = params.get('status_code')
        expected_result = params.get('expected_result')
        interfacecase_user = params.get('interfacecase_user')


        con = c.session()

        u = con.query(InterfaceAutoCase).order_by(InterfaceAutoCase.id.desc()).first()
        if u != None:
            info_id = case_id = int(u.id)+1
        else:
            info_id = case_id = 1
        try:
            InterfaceAutoCase_add = InterfaceAutoCase(class_id=class_id,id=info_id,case_mode=case_mode,case_name=case_name,
                            request_mode=request_mode,request_type=request_type,request_parameter=json.dumps(request_parameter),
                            request_head=json.dumps(request_head),target_key=target_key,is_valid=is_valid,is_execute=is_execute,
                            precondition=precondition,status_code=status_code,expected_result=expected_result,
                            interfacecase_user=interfacecase_user,case_url=case_url,case_id=case_id,modification_time=modification_time
                                                      )
            con.add(InterfaceAutoCase_add)
            con.commit()

            return '测试用例添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加测试用例添失败，请检查参数', 400

