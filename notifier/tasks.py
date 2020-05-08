from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time
from .bot import NotifyBot

logger = get_task_logger(__name__)
app = Celery('periodic', broker="pyamqp://guest@localhost//")
bot = NotifyBot()

@app.task
def get_task():
    bot.run_notifier()
    

app.conf.beat_schedule = {
    "task-announce": {
        "task": "task.get_task",
        "schedule": crontab(minute='*/1'),
        'args': None,
    }
}

app.conf.timezone = 'Asia/Dhaka'