from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time
from bot import NotifyBot

logger = get_task_logger(__name__)

app = Celery("periodic", broker="pyamqp://guest@localhost//")
task_bot = NotifyBot()

@app.task
def get_task():
    try:
        local_time = time.strftime("%H:%M", time.localtime())
        current_task = task_bot.get_current_task()
        if len(current_task) > 0 and local_time == current_task[1]:
            task_bot.run_notifier(current_task)
    except:
        print("There are some error! Check tasks.csv file")


app.conf.beat_schedule = {
    "task-announce": {
        "task": "tasks.get_task",
        "schedule": crontab(minute="*/1"),
        "args": None,
    }
}

app.conf.timezone = "Asia/Dhaka"
