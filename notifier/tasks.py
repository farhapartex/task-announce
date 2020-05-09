from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time
from bot import NotifyBot

logger = get_task_logger(__name__)
app = Celery("periodic", broker="pyamqp://guest@localhost//")
task_bot = NotifyBot()

# print("Hasan working")
@app.task
def get_task():
    local_time = time.strftime("%H:%M", time.localtime())
    current_task = task_bot.get_current_task()
    if local_time == current_task[1]:
        task_bot.run_notifier(current_task)


app.conf.beat_schedule = {
    "task-announce": {
        "task": "tasks.get_task",
        "schedule": crontab(minute="*/1"),
        "args": None,
    }
}

app.conf.timezone = "Asia/Dhaka"
