#!/usr/bin/env python

import os
from .files import check_file_exists, create_file
from .bot import NotifyBot


def check_args(args):
    if len(args) > 1:
        if args[0] == "init.py":
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
                bot = NotifyBot()
                bot.run_notifier()
