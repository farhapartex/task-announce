import notify2
import os, sys, time
from files import get_task_data


class NotifyBot:
    def __init__(self):
        notify2.init("Task Notifier")
        self._notify = None
        self.task_data = []

        self.get_ready_notifier()
        self.set_task_data()

    def get_ready_notifier(self):
        self._notify = notify2.Notification(None, icon="")
        self._notify.set_urgency(notify2.URGENCY_NORMAL)
        self._notify.set_timeout(10000)

    def set_task_data(self):
        self.task_data = get_task_data()

    def get_current_task(self):
        try:
            task = self.task_data[0]
            task_time = task[1].split()

            if task_time[1] == "am" or task_time[1] == "AM":
                task_time = task_time[0]
            elif task_time[1] == "pm" or task_time[1] == "PM":
                task_time = task_time[0].split(":")
                task_time = str(int(task_time[0]) + 12) + ":" + task_time[1]

            return [task[0], task_time]
        except:
            pass

    def run_notifier(self, current_task):
        self._notify.update(
            "Task: {0}".format(current_task[0]),
            "Task time: {0}".format(current_task[1]),
        )
        self._notify.show()
        time.sleep(7)
        del self.task_data[0]
