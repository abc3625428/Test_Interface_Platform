from flask import request
import os
from datetime import datetime
import logging
import logging.handlers

from logging import getLogger

logger = getLogger()



class RequestFormatter(logging.Formatter):
    """
    针对请求信息的日志格式
    """
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_logger(app):
    """
    设置日志
    :param app: Flask app对象
    :return:
    """

    # with app.app_context():  # Create an :class:`~flask.ctx.AppContext`.
    #     a = current_app
    #     d = current_app.config['DEBUG']
    logging_file_dir = app.config['LOGGING_FILE_DIR']
    logging_file_max_bytes = app.config['LOGGING_FILE_MAX_BYTES']
    logging_file_backup = app.config['LOGGING_FILE_BACKUP']
    logging_level = app.config['LOGGING_LEVEL']

    flask_console_handler = logging.StreamHandler()
    flask_console_handler.setFormatter(logging.Formatter('%(levelname)s %(module)s %(lineno)d %(message)s'))

    request_formatter = RequestFormatter('[%(asctime)s] %(remote_addr)s requested %(url)s\n'
                                         '%(levelname)s in %(module)s %(lineno)d: %(message)s')

    flask_file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(logging_file_dir, 'Account_unsealing.log'),
        maxBytes=logging_file_max_bytes,
        backupCount=logging_file_backup
    )
    flask_file_handler.setFormatter(request_formatter)

    limit_file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(logging_file_dir, 'limit.log'),
        maxBytes=logging_file_max_bytes,
        backupCount=logging_file_backup
    )
    limit_file_handler.setFormatter(request_formatter)

    log_flask_app = logging.getLogger('flask.app')
    log_flask_app.addHandler(flask_file_handler)
    log_flask_app.setLevel(logging_level)

    log_flask_limiter = logging.getLogger('flask-limiter')
    log_flask_limiter.addHandler(limit_file_handler)
    log_flask_limiter.setLevel(logging_level)

    # 埋点日志
    trace_file_handler = logging.FileHandler(
        os.path.join(logging_file_dir, 'UserClick.log')
    )
    trace_file_handler.setFormatter(logging.Formatter('%(message)s'))
    log_trace = logging.getLogger('trace')
    log_trace.addHandler(trace_file_handler)
    log_trace.setLevel(logging_level)

    # if app.debug:
    #     log_flask_app.addHandler(flask_console_handler)
    #     log_flask_limiter.addHandler(flask_console_handler)


def write_trace_log(param, read_time='', channel_id=0):
    """
    写埋点日志
    :param read_time: 阅读时间
    :param param: 埋点参数
    :param channel_id: 频道id
    """
    logger = logging.getLogger('trace')
    message = '{{"actionTime":"{action_time}","readTime":"{read_time}","channelId":{channel_id},"param":{param}}}'.format(
        action_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        read_time=read_time,
        channel_id=channel_id,
        param=param
    )
    logger.error(message)




