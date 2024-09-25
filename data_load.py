
import pandas as pd

def data_load_func(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

