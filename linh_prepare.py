import numpy as np
import pandas as pd

def encoding_columns(df):
    #create a column list for for loop below:
    col_list= ['self_employed', 'family_history', 'treatment', 'remote_work', 'tech_company', 'obs_consequence']
    for col in col_list:
        df[col] = df[col].map({'No': 0, 'Yes': 1})
    return df