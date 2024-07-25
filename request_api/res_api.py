from flask_restful import Resource,request
from flask_restful.reqparse import RequestParser
from flask import jsonify
import requests
import json
import log

import pdq_requests
from json_analysis import get_value,get_jsonvalue,res_get_value
from ymlrw import YamlUtils
from str_join_together import cookie_join_together
import sport
import pdq_requests
from models import RoutingSqlAlchemy
from models.user import db,UserAccountData

c = RoutingSqlAlchemy()

class USER_ACCOUNT_DATA_LOGIN(Resource):

    #pdq登录
    def post(self):
        result = []
        it = {}
        data = request.get_json()
        if data == None:
            res = pdq_requests.updatacookie()
            it['cookie'] = res
            result.append(it)

            return result,200
        else:
            loginName = data.get('loginName')
            loginPwd = data.get('loginPwd')

            if loginName and loginPwd:
                return pdq_requests.pdq_login(loginName,loginPwd),200
            else:
                return {"message":"无效的账号/密码"}

    def get(self):
        res = pdq_requests.get_userid()
        con = c.session()

        for i in res:


            mobile = 18515463110
            user_name = '王开源'
            email = 'wangkaiyuan@liepin.com'
            account = i
            user_id = 1
            user_add = UserAccountData(phone=mobile, user_name=user_name, email=email, account=account, user_id=user_id)

            con.add(user_add)
        try:
            con.commit()
            return ['数据写入成功'],200
        except IOError as e:
            return ['数据写入失败'],500


class USER_DATA_UNSEALING(Resource):

    def post(self):
        body = request.get_json()
        print(body,type(body))
        id = body.get('id')

        result = []
        con = c.session()
        users = con.query(UserAccountData.account).filter(UserAccountData.user_id==id).all()
        print(users)

        for i in list(users):
            user_acc = {}
            user_acc['account'] = i.account
            result.append(user_acc)
        return result,200


class USER_DATA_UNSEALING_DEL(Resource):

    def post(self):

        body = request.get_json()
        user_name = body.get('user_name')

        result = ['ok']
        con = c.session()

        users = con.query(UserAccountData).filter(UserAccountData.user_name==user_name).all()
        if users == []:
            return {'message':'User does not exist','code':-1,},400

        for user in users:
            con.delete(user)
            con.commit()

        return result,200