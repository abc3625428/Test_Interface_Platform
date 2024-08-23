from flask_restful import Resource
import log

from models.questing_table import AllQuestingReport
from models import RoutingSqlAlchemy


logger = log.getLogger('trace')

c = RoutingSqlAlchemy()

class GETSTATISTICS2(Resource):

    def get(self):

        con = c.session()

        classCount0 = con.query(AllQuestingReport).filter(AllQuestingReport.question_class == 0).count()
        classCount1 = con.query(AllQuestingReport).filter(AllQuestingReport.question_class == 1).count()
        classCount2 = con.query(AllQuestingReport).filter(AllQuestingReport.question_class == 2).count()
        classCount3 = con.query(AllQuestingReport).filter(AllQuestingReport.question_class == 3).count()

        levelCount0 = con.query(AllQuestingReport).filter(AllQuestingReport.question_level == 0).count()
        levelCount1 = con.query(AllQuestingReport).filter(AllQuestingReport.question_level == 1).count()
        levelCount2 = con.query(AllQuestingReport).filter(AllQuestingReport.question_level == 2).count()
        levelCount3 = con.query(AllQuestingReport).filter(AllQuestingReport.question_level == 3).count()


        result = {

            "goods":[
            {"label": "接口问题","value": classCount0},
            {"label": "策略问题", "value": classCount1},
            {"label": "性能问题", "value": classCount2},
            {"label": "客户端问题", "value": classCount3}
            ],

            "order":[
            {"label": "最高级问题", "value": levelCount0},
            {"label": "阻塞性问题", "value": levelCount1},
            {"label": "流程性问题", "value": levelCount2},
            {"label": "一般性问题", "value": levelCount3}
            ]

        }
        return result,200