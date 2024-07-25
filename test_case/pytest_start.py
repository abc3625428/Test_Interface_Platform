

import pytest
import os
from aig_requests_all.aig_requests_cpc import aig_cpc_search_loginout,co







if __name__ == '__main__':

    from datetime import datetime
    pytest.main(['-vs','test_case_start_execution','--durations= 10','--maxfail= 20',
                 '--html= aig_automated_test_report/{}.html'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")),'--self-contained-html'
                 ])
    co.stop()
    co.save()
    co.report()