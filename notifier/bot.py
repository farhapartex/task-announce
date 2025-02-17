import notify2
import os, sys, time
from notifier.files import BASE_DIR, get_task_data, delete_file
from scrapper.scrapper import Scrapper
from playsound import playsound


class NotifyBot:
    def __init__(self):
        notify2.init("Task Notifier")
        self._notify = None
        self.task_queue = get_task_data() if len(get_task_data()) > 0 else []

        self.get_ready_notifier()


    def get_ready_notifier(self):
        self._notify = notify2.Notification(None, icon="")
        self._notify.set_urgency(notify2.URGENCY_NORMAL)
        self._notify.set_timeout(10000)


    def get_current_task(self):
        try:
            task = self.task_queue[0]
            task_time = task[1].split()

            if task_time[1] == "am" or task_time[1] == "AM":
                task_time = task_time[0]
            elif task_time[1] == "pm" or task_time[1] == "PM":
                task_time = task_time[0].split(":")
                task_time = str(int(task_time[0]) + 12) + ":" + task_time[1]

            return [task[0], task_time]
        except:
            return []


    def run_notifier(self, current_task):

        # self._notify.update(
        #         "Task: {0}".format(current_task[0]),
        #         "Task time: {0}".format(current_task[1]),
        #     )

        if current_task[0] == 'news_headline':
            scraper = Scrapper()
            head_lines = " | ".join(scraper.get_news_headline())
            self._notify.update(
                "Task: {0}".format(head_lines),
                "Task time: {0}".format(current_task[1]),
            )
        else:
            self._notify.update(
                "Task: {0}".format(current_task[0]),
                "Task time: {0}".format(current_task[1]),
            )

        self._notify.show()
        time.sleep(7)
        os.chdir(BASE_DIR + "/settings")
        playsound("GunSound.mp3")
        time.sleep(7) if current_task[0] == 'news_headline' else time.sleep(3)
        del self.task_queue[0]
        if len(self.task_queue)==0: delete_file()
