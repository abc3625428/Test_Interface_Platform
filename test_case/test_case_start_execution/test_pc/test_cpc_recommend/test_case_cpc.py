import requests
import pytest

from aig_requests_all.aig_requests_cpc import test_aig_cpc_recommend
from aig_get_value_tool import aig_get_target_value

class Test_aig_cpc_recommend_homepage():


    paramter_expectDq = [
                    ('010', 'expectDq', '北京'),
                    ('020', 'expectDq', '上海'),
                    ('030', 'expectDq', '天津'),
                    ('040', 'expectDq', '重庆'),
                    ('050020', 'expectDq', '广州'),
                    ('050090', 'expectDq', '深圳'),
                    ('060080', 'expectDq', '苏州'),
                    ('060020', 'expectDq', '南京'),
                    ('070020', 'expectDq', '杭州'),
                    ('210040', 'expectDq', '大连'),
                    ('280020', 'expectDq', '成都'),
                    ('170020', 'expectDq', '武汉'),
                    ('270020', 'expectDq', '西安'),
                    ('260050', 'expectDq', '运城'),
                    ('250070', 'expectDq', '青岛'),
                    ('310020', 'expectDq', '昆明'),
                    ('250100', 'expectDq', '威海'),
                                            ]

    @pytest.mark.parametrize('expectDq, key, target',paramter_expectDq)
    def test_aig_cpc_recommend(self, expectDq, key, target):
        res = test_aig_cpc_recommend(expectDq= expectDq)
        li = aig_get_target_value(res, key)
        print(li)

        for i in li:
            assert  target in i



