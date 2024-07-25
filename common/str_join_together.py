



def cookie_join_together(cookie):
    str = ''
    for key,value in cookie.items():
        if key =='acs_ck_timeout':
            str = str + 'acs_ck_timeout' + '=' + value
        elif key=='acs_auth':
            str = str  + 'acs_auth'+ '=' + value + ';'
    return str

def cpc_cookie_join_together(cookie):
    str = ''
    for key,value in cookie.items():
        if key =='lt_auth':
            str = str + 'lt_auth' + '=' + value
        elif key=='acs_auth':
            str = str  + 'acs_auth'+ '=' + value + ';'
    return str