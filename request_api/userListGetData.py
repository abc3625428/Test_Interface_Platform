from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log
import datetime

from models.user import db,UserAccountData,User,Role
from models.user import db,UserAccountData
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class USERLISTGETDATA(Resource):


    def post(self):

        # data = request.get_json()
        #
        # print(data)
        #
        # username = data.get('username')
        # password = data.get('password')

            result = {"user_time":20240311,
                      "user_name":"御弟哥哥",
                      "user_avatar":"url",
                      "1":"1",
                      "ruleNames":[111],
                      "menus":[{'name':"后台管理",'icon':"help",'child':[{'name':"主控台",'icon':"home-filled",'frontpath':"/",},{'name':"数据中心",'icon':"home-filled",'frontpath':"/",},{'name':"用户中心",'icon':"home-filled",'frontpath':"/",},{'name':"物料中心",'icon':"home-filled",'frontpath':"/",},],},{'name':"Interface",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/goods/list",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"策略测试",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据召回",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"性能测试",'icon':"help",'child':[{'name':"测试总览",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试结果统计",'icon':"shopping-bag",'frontpath':"/",},{'name':"线上流量录制",'icon':"shopping-bag",'frontpath':"/",},{'name':"测试用例管理",'icon':"shopping-bag",'frontpath':"/",},{'name':"数据大盘展示",'icon':"shopping-bag",'frontpath':"/",},],},{'name':"系统设置",'icon':"help",'child':[{'name':"UI设置",'icon':"home-filled",'frontpath':"/",},{'name':"展示设置",'icon':"home-filled",'frontpath':"/",},],},]
                      }
            return result,200

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
            r = con.query(User).offset(offset_data).limit(per_page)
            totalCount = con.query(User).count()

        else:

            offset_data = (page - 1) * per_page
            totalCount = con.query(User).filter(User.user_name.like(f'%{search_keyword}%')).count()
            r = con.query(User).filter(User.user_name.like(f'%{search_keyword}%')).offset(offset_data).limit(per_page)

        for element in r:

            role_data = {}
            element_data = {}
            element_data['id'] = element.id
            element_data['avatar'] = element.avatar
            element_data['status'] = element.status
            element_data['super'] = element.is_admin
            element_data['create_time'] = element.creation_time
            element_data['update_time'] = element.modification_time
            element_data['username'] = element.user_name
            roledata = con.query(Role).filter(element.belonging_role==Role.id).first()
            role_data['id'] = roledata.id
            role_data['name'] = roledata.name
            element_data['role'] = role_data

            rr.append(element_data)


        re = con.query(Role)
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


class USER_ADD(Resource):

    def post(self):

        params = request.get_json()

        if params.get('password') is None or params.get('username') is None or params.get('status') is None or params.get('role_id') is None:
            return '请检查参数', 405

        print(params)


        user_name = params.get('username')
        status = params.get('status')
        is_admin = 0
        password = params.get('password')
        belonging_role = params.get('role_id')
        avatar = params.get('avatar')

        modification_time = creation_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        username = 'wangkaiyuan@liepin.cn'


        con = c.session()
        u = con.query(User).order_by(User.id.desc()).first()
        if u != None:
            info_id = user_id = int(u.id)+1
        else:
            info_id = user_id = 1
        try:
            user_add = User(user_name=user_name,id=user_id,status=status,is_admin=is_admin,password=password,
                            belonging_role=belonging_role,avatar=avatar,creation_time=creation_time,
                            modification_time=modification_time,info_id=info_id,username=username)
            con.add(user_add)
            con.commit()

            return '用户添加成功', 200

        except IOError as e:
            print(e,'捕获异常')
            return '添加用户失败，请检查参数', 400


class USER_DELETE(Resource):

    def post(self,id):

        params = request.get_json()
        con = c.session()
        try:
            con.query(User).filter(User.id == id).delete()
            con.commit()

        except IOError as E:
            return E,500

        return '用户删除成功',200


class USERSEARCH(Resource):

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
        r = con.query(User).filter_by(user_name=keyword).all().offset(offset_data).limit(per_page)
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
            element_data['username'] = element.user_name
            roledata = con.query(Role).filter(element.belonging_role == Role.id).first()
            role_data['id'] = roledata.id
            role_data['name'] = roledata.name
            element_data['role'] = role_data

            rr.append(element_data)

        re = con.query(Role)
        res = []

        for element in re:
            role_data = {}
            role_data['id'] = element.id
            role_data['name'] = element.name
            res.append(role_data)

        result = {}

        totalCount = con.query(User).filter_by(user_name=keyword).count()

        result['list'] = rr
        result['roles'] = res
        result['totalCount'] = totalCount

        logger.info('数据取回结果信息:{}'.format(result))

        return result, 200

