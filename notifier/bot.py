import notify2
import os, sys, time
from .files import get_task_data


class NotifyBot:
    def __init__(self):
        notify2.init("Task Notifier")
        self._notify = notify2.Notification(None, icon="")
        self._notify.set_urgency(notify2.URGENCY_NORMAL)
        self._notify.set_timeout(10000)

    def run_notifier(self):
        task_data = get_task_data()
        if len(task_data) > 0:
            for data in task_data:
                self._notify.update(
                    "Task: {0}".format(data[0]), "Task time: {0}".format(data[1])
                )
                self._notify.show()
                time.sleep(7)
        else:
            print("No task found")
