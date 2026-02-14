import pandas as pd

def load_transactions(path):
    df= pd.read_excel(path)
    df.columns = df.columns.str.lower()
    return df
