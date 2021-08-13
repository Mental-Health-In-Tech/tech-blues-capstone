import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def column_lower(df):
    df = df.rename(columns = {'Timestamp':'timestamp',
                                'Age':'age',
                                'Gender':'gender',
                                'Country':'country'})
    return df
def clean_male(df):
    df.gender.replace(to_replace = ['M','Male','male','m','Male-ish',
                                    'maile','something kinda male?','Mal',
                                    'Male (CIS)', 'Make','Guy (-ish) ^_^',
                                    'Male ','Man','msle','Mail','cis male',
                                    'Malr','Cis Man','Cis Male',
                                    'ostensibly male, unsure what that really means'],
                                    value = 'male', inplace = True)
    return df
def clean_female(df):
    df.gender.replace(to_replace = ['Female','female','Femake','Female ',
                                       'cis-female/femme','Woman','f','woman',
                                       'femail','Female (cis)','Cis Female','F'], value = 'female',
                                       inplace = True)
    return df

def clean_other(df):
    df.gender.replace(to_replace = ['Trans-female','queer/she/they','non-binary',
                                       'Nah','All','Enby','fluid','Genderqueer',
                                       'Androgyne','Agender','male leaning androgynous',
                                       'Trans woman','Neuter','Female (trans)', 'queer',
                                       'A little about you', 'p'],  value = 'other',
                                       inplace = True)
    return df

def remove_countries(df):
    countries = ['United States','Canada','Mexico','Switzerland',
                                   'Germany','Ireland','Poland','Austria','Italy',
                                   'Sweden','Spain','Norway','Czech Repulbic','Denmark',
                                   'Latvia','Moldova','Georgia','Romania','Finland','Bulgaria',
                                   'France','Slovenia','Russia','Bosnia and Herzegovina']
    df = survey_og[survey_og['country'].isin(countries)]
    return df

def fill_work_nulls(df):
    df.work_interfere.fillna(value = 'Not applicable', inplace = True)
    return df

def encode_gender(df):
    return df.gender.map({'male':0,'female':1,'other':2})

def encode_work(df):
    return df.work_interfere.map({'Never':0,'Not Applicable':0, 'Rarely':1,'Sometimes':1,'Often':1})

def encode_care(df):
    return df.care_options.map({'No':0,'Yes':1,'Not sure':3})

def encode_coworkers(df):
    return df.coworkers.map({'No':0, 'Yes':1, 'Some of them':2})

def encode_supervisor(df):
    return df.supervisor.map({'No':0, 'Yes':1, 'Some of Them':2})