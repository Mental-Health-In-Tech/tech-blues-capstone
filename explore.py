# Tech Blues Capstone Explore Module

# imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


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