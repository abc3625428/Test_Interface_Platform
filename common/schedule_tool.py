import schedule
import time
import threading

from request_api import res_api

class Timer:
    def __init__(self, function):
        self.function = function
        self.is_running = False
        self.thread = None

    def start(self):
        if self.is_running:
            raise ValueError("Timer is already running")
        self.is_running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self):
        if not self.is_running:
            raise ValueError("Timer is not running")
        self.is_running = False
        self.thread.join()

    def _run(self):
        while self.is_running:
            schedule.run_pending()
            time.sleep(1)

    def schedule_job(self, hour, minute, day):
        schedule.every().day.at(f"{hour}:{minute}")

