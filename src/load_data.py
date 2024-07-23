import pandas as pd
from .config import DATA_PATH

def load_data():
    data = pd.read_csv(DATA_PATH)
    print(data.shape)
    return data.head()
