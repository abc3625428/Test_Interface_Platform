from flask import request,jsonify,render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import log

from models.user import db,User
from models import RoutingSqlAlchemy
import parser
from flask import current_app
from get_token import generate_token

logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class USER_LOGIN(Resource):


    def post(self):

        data = request.get_json()

        print(data)

        username = data.get('username')
        password = data.get('password')
        us = {'msg':'用户名错误'}
        pss = {'msg':'密码错误'}

        con = c.session()
        res = con.query(User).filter_by(username=username).first()


        if res == None:
            return us,400



        ps = res.password
        print(ps)

        if int(ps) != int(password):
            return pss,400
        else:

            token = generate_token()
            result = {"user_time":20240311,"token":token,"msg":'用户登录成功'}
            return result,200

    def get(self):

        result = {"user": "wky","user_time":20240311}
        return result,200