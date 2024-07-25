
from models import db

import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base,declared_attr
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index,BigInteger
from sqlalchemy.orm import attributes
import time
import hashlib

class User(db.Model):

    __tablename__ = 'user_basic'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(50),nullable=False)
    status = db.Column(db.Integer,default=1)
    is_admin = db.Column(db.Integer,default=0)
    username = db.Column(db.String(20),default=0)
    password = db.Column(db.String(20),default=0)
    belonging_role = db.Column(db.String(20),default=0)
    avatar = db.Column(db.String(20),default=0)
    creation_time = db.Column(db.String(20),default=0)
    modification_time = db.Column(db.String(20),default=0)
    info_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

class UserInfo(db.Model):

    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=18)
    mobile = db.Column(db.BigInteger,nullable=False)
    email = db.Column(db.String(50))
    is_verified = db.Column(db.Integer,default=0)
    last_login = db.Column(db.DateTime, default=datetime.datetime.now)
    certificate = db.Column(db.DateTime, default=datetime.datetime.now)
    introduction = db.Column(db.String(50))
    profile_photo = db.Column(db.String(100),default=1)
    competence = db.Column(db.Integer, default=1)
    account = db.Column(db.String(50))
    gender = db.Column(db.Integer, default=0)

class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))


    # @declared_attr
    # def username_hash(cls):
    #     # 在插入记录之前生成一个唯一的哈希值作为 username 的值
    #     return db.Column(db.String(80), unique=True, default=lambda: hashlib.sha256(
    #         cls.User.certificate + str(time.time()).encode('utf-8')).hexdigest())
    #
    # @attributes.register_for_events(User)
    # def after_insert(mapper, connection, target):
    #     # 在插入记录之后设置 username_hash 字段为不可修改
    #     target.username_hash = None


# 用户数据表
class UserAccountData(db.Model):

    __tablename__ = 'user_account_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    phone = db.Column(db.BigInteger)
    email = db.Column(db.String(50))
    account = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    c = db.Column(db.String(100))



# def init_db():
#     """
#     创建数据库表
#     """
#     engine = create_engine(
#         "mysql+pymysql://root:123456@127.0.0.1:3306/data_master?charset=utf8",
#         max_overflow=0,  # 超过连接池大小外最多创建的连接
#         pool_size=5,  # 连接池大小
#         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
#     )
#
#     c = db.metadata.create_all(engine)
#     return c









#
#     def to_json(self):
#         dict_ = self.__dict__
#         if "_sa_instance_state" in dict_:
#             del dict_["_sa_instance_state"]
#         return dict_