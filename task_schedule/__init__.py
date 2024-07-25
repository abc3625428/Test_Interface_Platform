


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor


executors = {
    'defult': ProcessPoolExecutor(20)
}

scheduler = BlockingScheduler(executors=executors)

from pdq_task import acc_uni,test_logging,test_logging

# """
# 添加启动任务
# """
# scheduler.add_job(acc_uni,'date', runder='')
# scheduler.add_job(acc_uni,'interval',seconds=3)
# scheduler.add_job(acc_uni,'cron', day_of_week ="0-5", hour="6,12")
# scheduler.add_job(test_logging,'interval',seconds=5)
scheduler.add_job(test_logging,'interval',seconds=5)


if __name__ == '__main__':

    scheduler.start()