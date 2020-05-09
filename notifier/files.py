from pathlib import Path
import pandas as pd
import numpy as np
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)


def check_file_exists():
    return True if Path(BASE_DIR + "/tasks.csv").is_file() else False


def create_file(data):
    try:
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(BASE_DIR, "tasks.csv"), index=False)
        print("Task file created!")
        return True
    except:
        print("There are some error, try again!")
        return False


def get_task_data():
    try:
        if check_file_exists():
            df = pd.read_csv(BASE_DIR + "/tasks.csv")
            return df.values.tolist()
        else:
            print("file not found!")
            return []
    except:
        pass
