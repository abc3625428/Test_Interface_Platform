import requests

# 登录
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

    res = requests.post(url_post, data=data_post, headers=headers_post,verify=True)
    r = res.json()
    c = res.cookies
    # token = get_jsonvalue(r, "token")
    # YamlUtils.change_yml_only_data('TOKEN', token)
    # cookie = res.cookies

    return r,c

