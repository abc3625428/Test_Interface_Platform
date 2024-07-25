
import datetime
from pdq_requests import much_unsealing
from flask import current_app


def acc_uni():

    res =much_unsealing()
    if res == True:
        print(datetime.datetime.now())

def test_logging():
    print(datetime.datetime.now())
    current_app.logger.info('测试+++++++++++++++++++++++++++++++')


