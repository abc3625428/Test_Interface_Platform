import requests
import pytest

from aig_get_value_tool import aig_get_target_value
from aig_str_connotation import str_connotation
from aig_requests_all.aig_requests_cpc import aig_cpc_search_loginout,co

class Test_aig_cpc_search_logginout():

    @classmethod
    def setup_class(cls):
        print('------------测试类之前执行初始化--------------')

    @classmethod
    def teardown_class(cls):
        print('------------测试类之后执行处理----------------')

    paramter_edu = [('040','requireEduLevel','本科'),
                    ('030','requireEduLevel', '硕士'),
                    ('020','requireEduLevel', 'MBA/EMBA'),
                    ('010','requireEduLevel', '博士'),
                    ('050', 'requireEduLevel', '大专'),
                    ('060', 'requireEduLevel', '中专/中技'),
                    ('080', 'requireEduLevel', '高中'),
                    ('090', 'requireEduLevel', '初中')
                                                        ]

    @pytest.mark.parametrize('edulevel,key,target',paramter_edu)
    def test_cpc_search_word_list_eduLevel(self, edulevel, key, target):
        res = aig_cpc_search_loginout(eduLevel=edulevel)
        li = aig_get_target_value(res, key)
        print(li)

        for i in li:
            assert  target in i


    paramter_dq   = [
                    ('010', 'dq', '北京'),
                    ('020', 'dq', '上海'),
                    ('030', 'dq', '天津'),
                    ('040', 'dq', '重庆'),
                    ('050020', 'dq', '广州'),
                    ('050090', 'dq', '深圳'),
                    ('060080', 'dq', '苏州'),
                    ('060020', 'dq', '南京'),
                    ('070020', 'dq', '杭州'),
                    ('210040', 'dq', '大连'),
                    ('280020', 'dq', '成都'),
                    ('170020', 'dq', '武汉'),
                    ('270020', 'dq', '西安'),
                    ('260050', 'dq', '运城'),
                    ('250070', 'dq', '青岛'),
                    ('310020', 'dq', '昆明'),
                    ('250100', 'dq', '威海'),
                                            ]


    @pytest.mark.parametrize('dp,key,target', paramter_dq)
    def test_cpc_search_word_list_dp(self, dp, key, target):
        res = aig_cpc_search_loginout(dp=dp)
        li = aig_get_target_value(res, key)
        print(li)

        for i in li:
            assert target in i

    paramter_ke   = [
                    ('产品经理', 'title', '产品'),
                    ('java', 'title', ['Java','java','JAVA','后端开发']),
                    ('测试', 'title', '测试'),
                    ('运营', 'title', '运营'),
                    ('销售', 'title', '销售'),
                    ('前端', 'title', '前端'),
                    ('机械师', 'title', '机械'),
                    ('项目经理', 'title', ['项目经理','PM']),
                    ('工程监理', 'title', '监理'),
                    ('新媒体', 'title', '新媒体'),
                    ('医疗', 'title', '医疗'),
                    ('教师', 'title', ['老师','教师']),
                    ('培训师', 'title', '培训'),
                    ('美容师', 'title', '美容'),
                    ('讲师', 'title', '讲师'),
                    ('安保人员', 'title', '安保'),
                    ('助理', 'title', '助理'),
                    ('算法工程师', 'title', '算法'),
                    ('自然语言处理', 'title', ['语言', 'NLP','模型','人工智能','算法']),
                    ('视觉设计', 'title', '视觉设计'),
                    ('材料工程师', 'title', '材料'),
                    ('环保工程师', 'title', ['环保','污','修复','环境']),
                    ('政府关系', 'title', ['政府','关系']),
                    ('数据标注', 'title', ['数据','标注']),
                    ('Python', 'title', ['Python', 'thon','后端','数据','软件']),
                    ('深度学习', 'title', ['深度','机械','算法','数据','智能']),
                    ('电池工程师', 'title', '电池'),
                    ('电气工程师', 'title', '电气'),
                    ('生产计划', 'title', ['生产', '计划']),
                    ('光伏技术工程师', 'title', ['光伏', '技术']),
                    ('工艺制造工程师', 'title', ['工艺', '制造']),
                    ('总经理', 'title', ['总经理', 'CEO']),
                    ('总监', 'title', ['总经理', '总监']),
                    ('秘书', 'title', ['助理', '秘书','文秘']),
                    ('设计师', 'title', ['设计', '艺术', '视觉']),
                                            ]


    @pytest.mark.parametrize('ke,key,target', paramter_ke)
    def test_cpc_search_word_list_ke(self, ke, key, target):
        res = aig_cpc_search_loginout(ke=ke)
        li = aig_get_target_value(res, key)
        print(li)

        no_target = [i for i in li if all(j not in i for j in target)]
        assert len(no_target)< 4, f"断言失败：召回职位={no_target}"


