import pandas as pd
import numpy as np
import requests


def drop_columns(df):
    df = df.drop(columns=('comment', 'state'))

    
# part of the column encoding    
def encoding1(df, col_list):
    col_list = ['mental_health_consequence', 'phys-health_consequence', 'mental_health_interview', 'phys_health_interview']   
    for col in col_list:
        df[col] = df[col].map({'No': 0, 'Yes': 1, 'Maybe': 2})
return df

