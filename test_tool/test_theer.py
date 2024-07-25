


import requests

import json


def aig_cpc_recommend():

    data= {"operateKind":"LOGIN","sortType":"PC_HP_MIX","selectedExpect":"{\"expectJobtitle\":\"N000012\",\"expectDq\":\"010\",\"modifytime\":\"1708411819000\",\"expectMonthSalaryUpper\":15000,\"expectMonthSalaryLower\":10000,\"expectSalmonths\":12,\"expectDqName\":\"昌都\",\"expectId\":200075376045,\"expectIndustry\":\"000\",\"expectIndustryName\":\"全部行业\",\"expectJobtitleName\":\"心理咨询师\",\"tabTitle\":\"心理咨询师\"}"}
    url = "https://api-c.liepin.com/api/com.liepin.csearch.home-recommend-job-new"

    header = {
        'X-Client-Type': 'web',
        'X-Fscp-Std-Info': '{"client_id": "40106"}',
        'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c35',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'lt_auth=6ukDaycAyl39tyWP22Za4qgejYqqUjnL8ytYhB5Vh9a6DqGx4P%2FnRQmHrbUA%2FioIqxN0dfgzMLf%2FN%2Bz5yXpO4kQX8VGnl4CzveWzz34DdvRcN8W2vfj%2BkszWe58clUAB8mNbtkI%3D'


    }

    re = requests.post(url=url, headers=header, data=data)

    return (re.json())




def aig_cpc_search():
    # ta = {"city": city, "dq": dp, "pubTime": pubTime, "currentPage": 0, "pageSize": 40, "key": ke, "suggestTag": "",
    #       "workYearCode": workYearCode, "compId": "", "compName": "", "compTag": "", "industry": "", "salary": salary,
    #       "jobKind": "", "compScale": "", "compKind": compKind, "compStage": compStage, "eduLevel": eduLevel}
    # re = json.dumps(ta).encode().decode('unicode_escape')

    url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
    data = {"mainSearchPcConditionForm": "{\"city\": \"410\", \"dq\": \"410\", \"pubTime\": \"\", \"currentPage\": 1, \"pageSize\": 40,\"key\": \"测试\", \"suggestTag\": \"\", \"workYearCode\": \"6\", \"compId\": \"\",\"compName\": \"\", \"compTag\": \"\", \"industry\": \"\", \"salary\": \"1$3\", \"jobKind\": \"1\",\"compScale\": \"\", \"compKind\": \"\", \"compStage\": \"\", \"eduLevel\": \"\",\"otherCity\": \"\"}",
            "passThroughForm": "{\"scene\": \"input\", \"skId\": \"\", \"fkId\": \"\", \"ckId\": \"wf66llskcd3lfhhxqob6e9dtj7oyhb10\"}"}

    header = {

        'X-Client-Type': 'web',
        'X-Fscp-Std-Info': '{"client_id": "40108"}',
        'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c33',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest'

    }

    re = requests.post(url=url, headers=header, data=data, verify=False)
    return re.json()

