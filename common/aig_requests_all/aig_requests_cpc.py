
import requests
import json
import coverage

from ymlrw import YamlUtils

co = coverage.coverage()
co.start()

def aig_cpc_search_loginout(city="040",dp="040",pubTime="",compKind="",ke="",compStage="",workYearCode="0",salary="0",eduLevel= "040"):


    ta = {"city":city,"dq":dp,"pubTime": pubTime,"currentPage": 0, "pageSize": 40, "key":ke, "suggestTag": "","workYearCode":workYearCode, "compId": "", "compName": "", "compTag": "", "industry": "", "salary": salary, "jobKind": "","compScale": "", "compKind": compKind,"compStage":compStage,"eduLevel":eduLevel}
    re = json.dumps(ta).encode().decode('unicode_escape')


    url = "https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
    data = {"mainSearchPcConditionForm":re,
            "passThroughForm":"{\"scene\": \"input\", \"skId\": \"\", \"fkId\": \"\", \"ckId\": \"wf66llskcd3lfhhxqob6e9dtj7oyhb10\"}"}

    header = {

        'X-Client-Type': 'web',
        'X-Fscp-Std-Info': '{"client_id": "40108"}',
        'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c33',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest'

    }

    re = requests.post(url=url, headers=header, data=data,verify=False)
    return re.json()


def test_aig_cpc_recommend(expectJobtitle='N000012', expectDq= '010', expectMonthSalaryUpper='20000', expectMonthSalaryLower='10000', expectSalmonths= '12', expectIndustry= '000', expectIndustryName= '全部行业', expectJobtitleName= 'Java', expectDqName= '北京', tabTitle= 'Java', operateKind='UP'):

    ta = {"expectJobtitle":expectJobtitle,"expectDq":expectDq,"expectId":200072064908,"expectMonthSalaryUpper":expectMonthSalaryUpper,"expectMonthSalaryLower":expectMonthSalaryLower,"expectSalmonths":expectSalmonths,"expectIndustry":expectIndustry,"expectIndustryName":expectIndustryName,"expectJobtitleName":expectJobtitleName,"expectDqName":expectDqName,"modifytime":"1703557511000","tabTitle":tabTitle}
    re = json.dumps(ta).encode().decode('unicode_escape')
    data=  {"selectedExpect": re,"operateKind":operateKind,"sortType":"PC_HP_MIX"}

    url = "https://api-c.liepin.com/api/com.liepin.csearch.home-recommend-job-new"

    cookie = YamlUtils.rade_yml_cookie_data('CPC_COOKIE')
    header = {

        'X-Client-Type': 'web',
        'X-Fscp-Std-Info': '{"client_id": "40106"}',
        'X-Fscp-Trace-Id': '0519960d-bf32-4c76-b6a0-f88b54ab3c33',
        'X-Fscp-Version': '1.1',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie

    }

    re = requests.post(url=url, headers=header, data=data,verify=False)
    return re.json()