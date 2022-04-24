import pandas as pd

def read_data(file):
    file_dict  = {'doc_sociodemo':'data/Doc_Con_Pre_sociodemo.feather'}
    return pd.read_feather(file_dict[file])
