#!/usr/bin/env python

import os, sys
from notifier.files import BASE_DIR, check_file_exists, create_file


def check_args(args):
    if len(args) > 1 and args[0] == "init.py":
        if args[1] == "tasks":
            data = []
            while True:
                task = input("Task Name: ")
                if task == "":
                    break
                task_time = input("Task Time: ")
                data.append({"task": task, "task_time": task_time})
                print("")

            response = create_file(data)
            print("File created" if response else "File not create")
        elif args[1] == "up":
            os.chdir(BASE_DIR)
            celery = os.system("celery -A tasks worker --beat --loglevel=info")
        # elif args[1] == "news":
        #     obj = Scrapper()
        #     obj.get_news_headline()
