import requests

import str_join_together

# 账号登录 cookie/token 获取

def login_cpc(tel=12911223339, smsCode=921004):

    url_post = "https://api-passport.liepin.com/api/com.liepin.passport.account.tel-sms-login"
    data_post = {"tel": tel, "smsCode": smsCode, "businessId": 1100100012}
    headers_post = {'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Fscp-Std-Info':'{"client_id": "40106"}',
                    'X-Fscp-Version':'1.1',
                    'X-Client-Type':'web',
                    'X-Requested-With':'XMLHttpRequest',
                    'X-Fscp-Trace-Id':'677034f1-3198-4935-b38b-04bab03563be'
                    }

    res = requests.post(url_post, data=data_post, headers=headers_post,verify=False)
    r = res.json()
    c = res.cookies


    cookies_dict = requests.utils.dict_from_cookiejar(c)
    cookie = str_join_together.cpc_cookie_join_together(cookies_dict)

    return cookie

print(login_cpc())