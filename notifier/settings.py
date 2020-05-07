#!/usr/bin/env python

import os
from .files import check_file_exists, create_file


def check_args(args):
    if len(args) > 1:
        if args[0] == "init.py" and args[1] == "tasks":
            data = []
            while True:
                task = input("Task Name: ")
                if task == "":
                    break
                task_time = input("Task Time: ")
                data.append({"task": task, "task_time": task_time})
                print("")

            d = create_file(data)
            print(d)
