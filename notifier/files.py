from pathlib import Path
import pandas as pd
import numpy as np
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_file_exists():
    return True if Path(BASE_DIR + "tasks.csv").is_file() else False


def create_file(data):
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(BASE_DIR, "tasks.csv"), index=False)
    return True
