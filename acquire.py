import pandas as pd
import numpy as np
import os

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

os.path.isfile('survey.csv')




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