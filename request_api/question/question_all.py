from flask import request
from flask_restful import Resource
import log
import datetime

from models.questing_table import AllQuestingReport
from models import RoutingSqlAlchemy

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class QUESTIONLISTGETDATA(Resource):

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
            r = con.query(AllQuestingReport).offset(offset_data).limit(per_page)
            totalCount = con.query(AllQuestingReport).count()

        else:

            offset_data = (page - 1) * per_page
            totalCount = con.query(AllQuestingReport).filter(AllQuestingReport.AllQuestingReport_name.like(f'%{search_keyword}%')).count()
            r = con.query(AllQuestingReport).filter(AllQuestingReport.AllQuestingReport_name.like(f'%{search_keyword}%')).offset(offset_data).limit(per_page)

        for element in r:

            role_data = {}
            element_data = {}
            element_data['question_class'] = element.question_class
            element_data['question_level'] = element.question_level
            element_data['question_state'] = element.question_state
            element_data['question_model'] = element.question_model
            element_data['question_fd_person'] = element.question_fd_person
            element_data['question_dw_person'] = element.question_dw_person
            element_data['question_frequency'] = element.question_frequency
            element_data['question_explain'] = element.question_explain
            element_data['question_fd_time'] = element.question_fd_time
            element_data['question_dw_time'] = element.question_dw_time
            element_data['question_port'] = element.question_port
            element_data['question_demand'] = element.question_demand

            # roledata = con.query(AllQuestingReport).filter(element.belonging_role==AllQuestingReport.id).first()
            # role_data['id'] = roledata.id
            # role_data['name'] = roledata.name
            # element_data['role'] = role_data

            rr.append(element_data)


        re = con.query(AllQuestingReport)
        res = []

        for element in re:

            role_data = {}
            role_data['id'] = element.id
            role_data['name'] = element.name
            res.append(role_data)

        result = {}



        result['list'] = rr
        result['roles'] = res
        result['totalCount'] = totalCount

        logger.info('数据取回结果信息:{}'.format(result))

        return result,200


class QUESTION_ADD(Resource):

    def post(self):

        params = request.get_json()

        if params.get('question_class') is None or params.get('question_level') is None or params.get('question_state') is None or params.get('question_model') is None:
            return '请检查参数', 405

        print(params)


        question_class = params.get('question_class')
        question_level = params.get('question_level')
        question_state = params.get('question_state')
        question_model = params.get('question_model')
        question_fd_person = params.get('question_fd_person')
        question_dw_person = params.get('question_dw_person')
        question_frequency = params.get('question_frequency')
        question_explain = params.get('question_explain')

        question_dw_time = question_fd_time =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        question_port = params.get('question_port')
        question_demand = params.get('question_demand')


        con = c.session()

        u = con.query(AllQuestingReport).order_by(AllQuestingReport.id.desc()).first()
        if u != None:
            info_id = AllQuestingReport_id = int(u.id)+1
        else:
            info_id = AllQuestingReport_id = 1
        try:
            AllQuestingReport_add = AllQuestingReport(question_class=question_class,id=AllQuestingReport_id,
                                                      question_level=question_level,question_fd_person=question_fd_person,question_dw_person=question_dw_person,
                            question_frequency=question_frequency,question_explain=question_explain,question_fd_time=question_fd_time,
                            question_dw_time=question_dw_time,question_port=question_port,question_demand=question_demand
                                                      ,question_state=question_state,question_model=question_model)
            con.add(AllQuestingReport_add)
            con.commit()

            return '缺陷添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加缺陷失败，请检查参数', 400


class QUESTION_DELETE(Resource):

    def post(self,id):

        params = request.get_json()
        con = c.session()
        try:
            con.query(AllQuestingReport).filter(AllQuestingReport.id == id).delete()
            con.commit()

        except IOError as E:
            return E,500

        return '缺陷删除成功',200


class QUESTIONSEARCH(Resource):

    def get(self, currentPage):

        params = request.get_json()
        print(params)



        if params.get('keyword') == None:
            return None
        keyword = params.get('keyword')

        if currentPage is None:
            page = 1
            per_page = 10
        else:
            page = int(currentPage)
            per_page = 10



        con = c.session()


        offset_data = (page - 1) * per_page
        r = con.query(AllQuestingReport).filter_by(AllQuestingReport_name=keyword).all().offset(offset_data).limit(per_page)
        rr = []

        for element in r:
            role_data = {}
            element_data = {}
            element_data['id'] = element.id
            element_data['avatar'] = element.avatar
            element_data['status'] = element.status
            element_data['super'] = element.is_admin
            element_data['create_time'] = element.creation_time
            element_data['update_time'] = element.modification_time
            element_data['AllQuestingReportname'] = element.AllQuestingReport_name
            roledata = con.query(AllQuestingReport).filter(element.belonging_role == AllQuestingReport.id).first()
            role_data['id'] = roledata.id
            role_data['name'] = roledata.name
            element_data['role'] = role_data

            rr.append(element_data)

        re = con.query(AllQuestingReport)
        res = []

        for element in re:
            role_data = {}
            role_data['id'] = element.id
            role_data['name'] = element.name
            res.append(role_data)

        result = {}

        totalCount = con.query(AllQuestingReport).filter_by(AllQuestingReport_name=keyword).count()

        result['list'] = rr
        result['roles'] = res
        result['totalCount'] = totalCount

        logger.info('数据取回结果信息:{}'.format(result))

        return result, 200


class QUESTION_MODIFY(Resource):

    def post(self):

        params = request.get_json()

        if params.get('question_class') is None or params.get('question_level') is None or params.get('question_state') is None or params.get('question_model') is None:
            return '请检查参数', 405

        print(params)


        question_class = params.get('question_class')
        question_level = params.get('question_level')
        question_fd_person = params.get('question_fd_person')
        question_dw_person = params.get('question_dw_person')
        question_frequency = params.get('question_frequency')
        question_explain = params.get('question_explain')

        question_dw_time = question_fd_time = creation_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        question_port = params.get('question_port')
        question_demand = params.get('question_demand')


        con = c.session()

        u = con.query(AllQuestingReport).order_by(AllQuestingReport.id.desc()).first()
        if u != None:
            info_id = AllQuestingReport_id = int(u.id)+1
        else:
            info_id = AllQuestingReport_id = 1
        try:
            AllQuestingReport_add = AllQuestingReport(question_class=question_class,id=AllQuestingReport_id,
                                                      question_level=question_level,question_fd_person=question_fd_person,question_dw_person=question_dw_person,
                            question_frequency=question_frequency,question_explain=question_explain,question_fd_time=question_fd_time,
                            question_dw_time=question_dw_time,question_port=question_port,question_demand=question_demand)
            con.add(AllQuestingReport_add)
            con.commit()

            return '缺陷添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加缺陷失败，请检查参数', 400