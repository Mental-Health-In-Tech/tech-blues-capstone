# Tech Blues Capstone Explore Module

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


def cat_vs_quant(df):
    '''
    This function takes in a pandas DataFrame, and returns lists of categorical and quantitative variables.
    '''
    df = df.drop(columns=(['timestamp', 'country']))
    cat_vars = []
    quant_vars = []
    col_list = list(df.columns)
    
    for col in col_list:
        if df[col].nunique()<=6:
            cat_vars.append(col)
        else:
            quant_vars.append(col)
    
    return cat_vars, quant_vars

######################## Mother Functions ######################################

def explore_univariate(df, cat_vars=[], quant_vars=[]):
    '''
    This function takes in a pandas DataFrame, a list of categorical variables, and a list of quantitative variables.
    It uses the 'explore_univariate_categorical' and 'explore_univariate_quantitative' functions to plot:
    - frequency tables and barplots for categorical data,
    - descriptive stats, histograms, and boxplots for quantitative variables.
    '''
    cat_vars, quant_vars = cat_vs_quant(df)
    
    for cat in cat_vars:
        explore_univariate_categorical(df, cat)
        print('_________________________________________________________________')
    for quant in quant_vars:
        p, descriptive_stats = explore_univariate_quant(df, quant)
        plt.show(p)
        print(descriptive_stats)
        
def explore_bivariate(df, target, cat_vars, quant_vars):
    '''
    This function takes in a pandas DataFrame, a target variable (as a string), a list of categorical variables,
    and a list of quntitative variables. It opperates on top of the 'explore_bivarite_categorical' and 
    'explore_bivariate_quantitative' functions to return:
    - categorical variables:
        - 
    - quantitative variables:
        - 
    '''
    for cat in cat_vars:
        explore_bivariate_categorical(df, target, cat)
    for quant in quant_vars:
        explore_bivariate_quant(df, target, quant)

def explore_multivariate(df, target, cat_vars, quant_vars):
    '''
    '''
    print('printing swarmgrid...')
    plot_swarm_grid_with_color(df, target, cat_vars, quant_vars)
    plt.show()
    print('making violin...')
    violin = plot_violin_grid_with_color(df, target, cat_vars, quant_vars)
    plt.show()
    print('making pairplot...')
    pair = sns.pairplot(data=df, vars=quant_vars, hue= target)
    plt.show()
    print('plotting continuous vars')
    plot_all_continuous_vars(df, target, quant_vars)
    plt.show()  
    
########################## Univariate #########################################
########### Can be done on entire dataset, or train ###########################
        
def explore_univariate_categorical(df, cat_var):
    '''
    This function takes in a pandas DataFrame, and a single categorical variable in the dataset,
    and returns a frequency table and barplot of the categorical variable.
    '''
    
    # makes the frequency table
    frequency_table = freq_table(df, cat_var)
    # sets the figure size for the barplot
    plt.figure(figsize=(4,4))
    # creates the barplot, ***color needs to be changed***
    sns.barplot(x=cat_var, y='Count', data=frequency_table, color='lightseagreen')
    # sets the title of the barplot based on the categorical variable
    plt.title(f'{cat_var} Bar Plot in Mental Heath Data')
    # shows the barplot
    plt.show()
    # prints the frequency table
    print(frequency_table)
    
def explore_univariate_quant(df, quant_var):
    '''
    This function takes in a pandas DataFrame, and a single quantitative variable, and returns
    descriptive stats table, histogram, and boxplot of the distributions. 
    '''
    # runs the descriptive stats of the quantitative variable
    descriptive_stats = df[quant_var].describe()
    # sets the figure size of the plot entire plot
    plt.figure(figsize=(12,4))
    # first subplot (top left) us the histogram of quant_var
    p = plt.subplot(1, 2, 1)
    # ***** Need to change the color ******************
    p = plt.hist(df[quant_var], color='lightseagreen')
    # sets the title for the histogram
    p = plt.title(f'{quant_var} Histogram in Mental Health Data')

    # second plot (top right): box plot
    p = plt.subplot(1, 2, 2)
    p = plt.boxplot(df[quant_var])
    # sets the title for the boxplot
    p = plt.title(f'{quant_var} Boxplot in Mental Health Data')
    return p, descriptive_stats

def freq_table(df, cat_var):
    '''
    This function takes in a pandas DataFrame, along with a single categorical variable.
    It computes the frequency count and percent split
    and return a dataframe of those values along with the different classes. 
    '''
    class_labels = list(df[cat_var].unique())

    frequency_table = (
        pd.DataFrame({cat_var: class_labels,
                      'Count': df[cat_var].value_counts(normalize=False), 
                      'Percent': round(df[cat_var].value_counts(normalize=True)*100,2)}
                    )
    )
    return frequency_table