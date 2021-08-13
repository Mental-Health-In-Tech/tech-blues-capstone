# Tyler's Section of Data Preparation

# imports
import pandas as pd
import requests
import numpy as np
from datetime import datetime

################ Tyler's Section as a Mother Function ########################

def tyler_prep(df):
    '''
    This is Tyler's section of initial prep for the Mental Health and Tech Capstone project. This a combination of the following functions:
    - 'to_datetime' that converts the Timestamp column to datetime
    - 'drop_age_outliers' that only keeps employees aged 18-85
    - 'encode_employee_count_bins' that encodes the already binned 'no_employees' and changes the name to 'company_size'
    
    **** These functions will only work if the column names have already been converted to lowercase ****
    '''
    # converts 'timestamp' to datetime
    df = to_datetime(df)
    # drops outliers/typos from 'Age'
    df = drop_age_outliers(df)
    # encodes 'no_employees' and canges name to 'company_size'
    df = encode_no_employee(df)
    
    return df

########################## Tyler's Child Functions ##############################

def to_datetime(df):
    '''
    This function takes in a pandas DataFrame and converts the target 'timestamp' column to datetime, and returns the DataFrame.
    '''
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def drop_age_outliers(df):
    '''
    This function takes in a pandas DataFrame, and removes all ages below 18 and over 85, and returns a pandas DataFrame with working-age employees only.
    '''
    # Drops those younger than 18
    df = df[df['age'] >= 18]
    # Drops those older than 85
    df = df[df['age'] <= 85]
    
    return df

def encode_no_employee(df):
    '''
    This function takes in a pandas DataFrame, and encodes the 'no_employee' column, renames the column 'company_size', and returns the updated pandas DataFrame.
    '''
    # encodes the already binned 'no_employees' column
    df['no_employees'] = df['no_employees'].map({'1-5': 0, '6-25': 1, '26-100': 2, '100-500': 3, '500-1000': 4, 'More than 1000': 5})
    # renames the column to 'company_size'
    df = df.rename(columns=({'no_employees': 'company_size'}))
    
    return df

####### Only Necessary if columns not already converted to lowercase #########

def convert_lower(df):
    '''
    This function takes in a pandas dataframe, converts all columns to lowercase, and returns the updated pandas DataFrame.
    '''
    # converts all column names to lowercase
    df.columns = df.columns.str.lower()
    
    return df

############################ Split The Data ##################################

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    
    return train, validate, test

def full_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    Then, train, validate, and test, have the target variable split out into a separate pandas Series.
    The function returns, X_tain, y_train, X_validate, y_validate, X_test, y_test where all 'X' are pandas DataFrames,
    and all 'y' are pandas Series. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    
    X_train = train.drop(columns=target)
    y_train = train[target]
    
    X_validate = validate.drop(columns=target)
    y_validate = validate[target]
    
    X_test = test.drop(columns=target)
    y_test = test[target]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test