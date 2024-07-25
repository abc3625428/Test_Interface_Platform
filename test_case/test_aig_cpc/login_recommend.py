

import requests
import pytest

from aig_get_value_tool import aig_get_target_value

class Test_unlogin():

    @classmethod
    def setup_class(cls):
        print('测试类之前执行')

    @classmethod
    def teardown_class(cls):
        print('测试类之后执行')

    # def test_cpc_recommend_data(self):
    #
    #     url_post = "https://api-c.liepin.com/api/com.liepin.csearch.home-recommend-job-new"
    #     data_post = {"data":{"operateKind":"UP","sortType":"PC_HP_MIX","selectedExpect":"{\"modifytime\":\"1701070279000\",\"expectJobtitle\":\"N000058\",\"expectDq\":\"280020\",\"expectId\":200068350477,\"expectMonthSalaryUpper\":18000,\"expectMonthSalaryLower\":11000,\"expectSalmonths\":13,\"expectIndustry\":\"000\",\"expectIndustryName\":\"全部行业\",\"expectJobtitleName\":\"测试工程师\",\"expectDqName\":\"成都\",\"tabTitle\":\"测试工程师\"}","existFallbackResult":False}}
    #     headers_post = {
    #                     "X-Client-Type":"web",
    #                     "X-Fscp-Std-Info":'{"client_id": "40108"}',
    #                     "X-Fscp-Trace-Id":"a500acec-f939-4df0-a5a1-7a9916c1c405",
    #                     "X-Fscp-Version":"1.1",
    #                     "X-Requested-With":"XMLHttpRequest"
    #                     }
    #
    #     res = requests.post(url_post, data=data_post, headers=headers_post,verify=True)
    #     r = res.json()
    #
    #     # token = get_jsonvalue(r, "token")
    #     # YamlUtils.change_yml_only_data('TOKEN', token)
    #     # cookie = res.cookies
    #
    #     print(r)
    #     return r
    #
    #
    # def test_cpc_search_filter_data(self):
    #
    #     url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
    #
    #     head = {
    #
    #         "X-Client-Type":"web",
    #         "X-Fscp-Std-Info":'{"client_id": "40108"}',
    #         "X-Fscp-Trace-Id":"a500acec-f939-4df0-a5a1-7a9916c1c405",
    #         "X-Fscp-Version":"1.1",
    #         "X-Requested-With":"XMLHttpRequest"
    #     }
    #     data = {"data":{"mainSearchPcConditionForm":{"city":"410","dq":"010","pubTime":"","currentPage":0,"pageSize":40,"key":"测试","suggestTag":"","workYearCode":"0","compId":"","compName":"","compTag":"","industry":"","salary":"","jobKind":"","compScale":"","compKind":"","compStage":"","eduLevel":"","otherCity":""},"passThroughForm":{"ckId":"u3eb3qx2pwyi23tbjueixc34610zh8y9","scene":"input","skId":"qniehhepyjp70vi05qq8y5a673fs1tub","fkId":"qniehhepyjp70vi05qq8y5a673fs1tub","sfrom":"search_job_pc"}}}
    #
    #
    #     res = requests.post(url,headers = head ,data=data,verify=True)
    #
    #     print(res.json())
    #
    # @pytest.mark.parametrize('target',list(range(1,30,1)))
    # def test_cpc_search_word_list(self,target):
    #
    #     url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-hot-search-word-list'
    #
    #     header = {
    #
    #         'X-Client-Type':'web',
    #         'X-Fscp-Std-Info': '{"client_id": "40108"}',
    #         'X-Fscp-Trace-Id': 'eab9a130-6d89-4170-9b36-a8ba3c6e1687',
    #         'X-Fscp-Version': '1.1',
    #         'X-Requested-With': 'XMLHttpRequest',
    #
    #     }
    #
    #     res = requests.get(url=url,headers=header,verify=True)
    #     print(res.json())
    #     assert res == target
    #
    # @pytest.mark.skipif(True,reason='测试跳过')
    # def test_test_skip(self):
    #     print('测试跳过用例')
    #     assert 1==2
    #
    @pytest.mark.parametrize(['key','target'],[('requireEduLevel'),('本科')])
    def test_cpc_search_word_list(self, key, target):

        url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

        data = {
            "mainSearchPcConditionForm": "{\"city\": \"410\", \"dq\": \"410\", \"pubTime\": \"\", \"currentPage\": 0, \"pageSize\": 40,\"key\": \"测试\", \"suggestTag\": \"\", \"workYearCode\": \"0\", \"compId\": \"\", \"compName\": \"\",\"compTag\": \"\", \"industry\": \"\", \"salary\": \"\", \"jobKind\": \"\", \"compScale\": \"\",\"compKind\": \"\", \"compStage\": \"\", \"eduLevel\": \"040\"}",
            "passThroughForm": "{\"scene\": \"input\", \"skId\": \"\", \"fkId\": \"\", \"ckId\": \"wf66llskcd3lfhhxqob6e9dtj7oyhb10\"}"}

        header = {

            'X-Client-Type':'web',
            'X-Fscp-Std-Info': '{"client_id": "40108"}',
            'X-Fscp-Trace-Id': 'eab9a130-6d89-4170-9b36-a8ba3c6e1687',
            'X-Fscp-Version': '1.1',
            'X-Requested-With': 'XMLHttpRequest',

        }

        res = requests.post(url=url, headers=header, data=data,verify=True)
        li = aig_get_target_value(res.json(), key)
        print(res,li)
        assert  target in li

if __name__ == '__main__':
    # 参数说明：
    # -k: 可以通过某些关键字进行匹配，从而执行哪些，不执行哪些（区分是否填写not）
    # -m: 为用例打标签，执行时可以被指定，使用时用例上添加 @ pytest.mark.自定义标记名
    # -x: 遇到错误用例，立即停止运行（后面的不再执行）
    # -s ：将print的内容打印出来
    # -v: 显示详细结果
    # -q: 显示简洁结果
    # -n: 多进程执行  需要pytest-xdist库
    #
    # 2进程各4线程执行（共8线程）'--workers=2','--tests-per-worker= 4' 需要pytest-parllel==0.0.10库 python 3.9不兼容
    # '--collect-only' 加载所有用例不执行
    # '--durations= 10' 执行用时最长的10个用例
    # --maxfail= n: 失败到达n次后，退出
    # --self-contained-html 不受css样式限制
    # --html = re1port.html 输出报告地址

    from datetime import datetime
    pytest.main(['-vs','login_recommend.py','--durations= 10','--maxfail= 30','-n= 2',
                 '--html= aig_automated_test_report/{}.html'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")),
                 '--self-contained-html'])