# testing wrangle functions

# Imports
import pandas as pd
import numpy as np
import os

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

os.path.isfile('survey.csv')

import requests
from typing import Mapping
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import acquire
import prepare

############################### Data Acquisition ##############################################

def get_survey_data(csv_file, cached=True):
    '''
    This function reads in external csv file for survey data and writes data to
    a csv file if cached == False or if cached == True reads in survey data from a csv file, returns df.
    '''
    df = pd.read_csv(csv_file)
    if cached == False or os.path.isfile('survey.csv') == False:
        # Read fresh data from url into a DataFrame.
        df = df
        # Write DataFrame to a csv file.
        df.to_csv('survey.csv')
    else:
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('survey.csv')
    return df


def overview(df):
    '''
    This function returns the shape and info of the df. It also includes a breakdown of the number of unique values
    in each column to determine which are categorical/discrete, and which are numerical/continuous. Finally, it returns
    a breakdown of the statistics on all numerica columns.
    '''
    print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('----------------------------------')
    print('')
    print(df.info())
    print('----------------------------------')
    print('')
    print('Unique value counts of each column')
    print('')
    print(df.nunique())
    print('----------------------------------')
    print('')
    print('Stats on Numeric Columns')
    print('')
    print(df.describe())
    
############################## Data Preparation #####################################################

def prep_the_strings(df):
    '''
    This function preps the mental health data through the use of a number of functions.
    '''
    df = prepare.convert_lower(df)
    df = prepare.to_datetime(df)
    df = prepare.drop_age_outliers(df)
    df = prepare.drop_columns(df)
    df = prepare.fill_work_nulls(df)
    df = prepare.clean_female(df)
    df = prepare.clean_male(df)
    df = prepare.clean_other(df)
    df = prepare.remove_countries(df)
    df = prepare.target_correction(df)
    df = prepare.employer_status(df)
    

    return df


def prep_encode(df):
    '''
    This function encodes the mental data into numeric values through a number of functions.
    '''
    
    df = prepare.encode_yes_no_dont_know(df)
    df = prepare.encode_yes_no_columns(df)
    df = prepare.encode_no_employee(df)
    df = prepare.encoding_no_yes_maybe(df)
    df = prepare.encode_supervisor(df)
    df = prepare.encode_coworkers(df)
    df = prepare.encode_care(df)
    df = prepare.encode_work(df)
    df = prepare.encode_leave(df)
    df = prepare.encode_gender(df)

    
    return df