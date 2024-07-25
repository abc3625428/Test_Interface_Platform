import pytest
from . import login_cpc

# scope表示作用域，autouse为true表示测试函数不必进行参数传递就可以生效
@pytest.fixture(scope='session', autouse=True)
def session_level():

    login_cpc()
    print("------所有用例前执行cpc cookie修改成功------")
    yield
    print("------所有用例后执行完毕 报告输出正常------")



##模块前后执行
# @pytest.fixture(scope='module', autouse=True)
# def module_level():
#     print("module==模块前执行一次")
#     yield
#     print("module==模块后执行一次")

##类前后执行
# @pytest.fixture(scope='class', autouse=True)
# def class_level():
#     print("class==类前执行一次")
#     yield
#     print("class==类后执行一次")
#
#
##函数前后执行
# @pytest.fixture(scope='function', autouse=True)
# def func_level():
#     print("function==函数前执行一次")
#     yield
#     print("function==函数后执行一次")