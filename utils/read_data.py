import pandas as pd

def read_data(file):
    file_dict  = {'doc_sociodemo':'data/Doc_Con_Pre_sociodemo.csv'}
    return pd.read_csv(file_dict[file], sep=';')
