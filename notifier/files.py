from pathlib import Path
import pandas as pd
import numpy as np
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_file_exists():
    return True if Path(BASE_DIR + "/tasks.csv").is_file() else False


def create_file(data):
    try:
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(BASE_DIR, "tasks.csv"), index=False)
        print("Task file created!")
        return True
    except:
        return False


def get_task_data():
    try:
        if check_file_exists():
            df = pd.read_csv(BASE_DIR + "/tasks.csv")
            return df.values.tolist()
        else:
            return []
    except:
        pass


def delete_file():
    try:
        os.chdir(BASE_DIR)
        os.system("rm -f tasks.csv")
    except:
        pass
