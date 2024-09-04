
from flask import Flask

def create_flask_app(config, enable_config_file=False):
    """
    创建Flask应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: Flask应用
    """
    app = Flask(__name__)
    app.config.from_object(config)


    return app


def create_app(config, enable_config_file=False):
    """
    创建应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: 应用
    """
    app = create_flask_app(config, enable_config_file)


    # 配置日志
    from log import create_logger
    create_logger(app)

    # 注册url转换器
    from converters import register_converters
    register_converters(app)

    # MySQL数据库连接初始化
    from models import db

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/data_master'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
    db.init_app(app)




    # # # 添加请求钩子
    # from middlewares import jwt_authentication
    # app.before_request(jwt_authentication)

    # 用户模块蓝图
    from request_api import user_bp,user_data,report
    app.register_blueprint(user_bp)
    app.register_blueprint(user_data)
    app.register_blueprint(report)

    # 缺陷模块蓝图
    from request_api.question import question_bp
    app.register_blueprint(question_bp)

    # 数据模块蓝图
    from request_api.database import data_bp
    app.register_blueprint(data_bp)

    #接口测试蓝图
    from request_api.interface import interface_bp
    app.register_blueprint(interface_bp)

    # 定期任务启动

    #解决请求跨域
    from flask_cors import CORS
    CORS(app, supports_credentials=True)

    return app