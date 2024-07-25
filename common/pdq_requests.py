import requests
import json
import log

from json_analysis import get_value, get_jsonvalue, res_get_value
from ymlrw import YamlUtils
from str_join_together import cookie_join_together
import sport



# 登录
def pdq_login(loginName="wangkaiyuan", loginPwd="3de2c272f20ca45c6a612e0bb85873b5"):

    url_post = "http://acs.tongdao.cn/auth/login.json"
    data_post = {"loginName": loginName, "loginPwd": loginPwd, "tenantCode": "acs"}
    headers_post = {"Content-Type": "application/x-www-form-urlencoded"}

    res = requests.post(url_post, data=data_post, headers=headers_post)
    r = res.json()
    token = get_jsonvalue(r, "token")
    YamlUtils.change_yml_only_data('TOKEN', token)
    cookie = res.cookies

    return cookie

#修改yml文件cookie
def updatacookie(loginName="wangkaiyuan", loginPwd="3de2c272f20ca45c6a612e0bb85873b5"):

    cookie = pdq_login(loginName=loginName, loginPwd=loginPwd)
    cookies_dict = requests.utils.dict_from_cookiejar(cookie)
    ck = cookie_join_together(cookies_dict)

    if ck != None:
        YamlUtils.change_yml_only_data('COOKIE',ck)
        return ck
    else:
        return '登录失败'


#获取pandQ人员数据
def get_userdata():

    cookie = YamlUtils.rade_yml_cookie_data()

    url_get = "https://testing.tongdao.cn/testdata/account/manage/list.json"
    params_get = {"tenant": "liepin", "curPage": "0","pageSize":"100"}
    headers_get = {
        "Workspace":"liepin",
        "Cookie": cookie

    }

    response_get = requests.get(url_get, params=params_get, headers=headers_get)
    res = response_get.json()

    return res

#解封对应人员的对应账号
def accountunsealing(id):

    cookie = YamlUtils.rade_yml_cookie_data()
    url_get = "http://testing.tongdao.cn/testdata/account/manage/enable.json"
    params_get = {"testAccountId": id}
    headers_get = {
        "Workspace":"liepin",
        "Cookie": cookie

    }
    response_get = requests.get(url_get, params=params_get, headers=headers_get)
    res = response_get.json()
    return res

def get_userid():

    res = get_userdata()
    return res_get_value(res,'id')

def much_unsealing():

    updatacookie()
    res = get_userid()
    for i in range(len(res)):
        accountunsealing(res[i])
    return True

