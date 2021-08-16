# Tyler's Data Exploration Module

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats

######################## Mother Functions ######################################

def explore_univariate(df, cat_vars, quant_vars):
    '''
    This function takes in a pandas DataFrame, a list of categorical variables, and a list of quantitative variables.
    It uses the 'explore_univariate_categorical' and 'explore_univariate_quantitative' functions to plot:
    - frequency tables and barplots for categorical data,
    - descriptive stats, histograms, and boxplots for quantitative variables.
    '''
    for cat in cat_vars:
        explore_univariate_categorical(df, cat)
        print('_________________________________________________________________')
    for quant in quant_vars:
        p, descriptive_stats = explore_univariate_quant(df, quant)
        plt.show(p)
        print(descriptive_stats)
        
def explore_bivariate(df, target, cat_vars=[], quant_vars=[]):
    '''
    This function takes in a pandas DataFrame, a target variable (as a string), a list of categorical variables,
    and a list of quntitative variables. It opperates on top of the 'explore_bivarite_categorical' and 
    'explore_bivariate_quantitative' functions to return:
    - categorical variables:
        - 
    - quantitative variables:
        - 
    '''
    
    cat_vars, quant_vars = cat_vs_quant(df)
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
    
def cat_vs_quant(df):
    '''
    This function takes in a pandas DataFrame, and returns lists of categorical and quantitative variables.
    '''
    df = df.drop(columns=(['timestamp', 'country', 'work_interfere']))
    cat_vars = []
    quant_vars = []
    col_list = list(df.columns)
    
    for col in col_list:
        if df[col].nunique()<=6:
            cat_vars.append(col)
        else:
            quant_vars.append(col)
    
    return cat_vars, quant_vars

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
    plt.figure(figsize=(2,2))
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
    plt.figure(figsize=(8,2))
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

############################ Bivariate Exploration ############################

############## This can be only be done on the train dataset ##################

#### Bivariate Categorical
        
def explore_bivariate_categorical(df, target, cat_var):
    '''
    This function takes in pandas DataFrame, a target variable (as a string) and a single categorical variable (as a string). It runs a chi-square test for the proportions and creates a barplot, adding a horizontal line of the overall rate of the target. 
    '''
    print(cat_var, "\n_____________________\n")
    ct = pd.crosstab(df[cat_var], df[target], margins=True)
    chi2_summary, observed, expected = run_chi2(df, cat_var, target)
    p = plot_cat_by_target(df, target, cat_var)

    print(chi2_summary)
    print("\nobserved:\n", ct)
    print("\nexpected:\n", expected)
    plt.show(p)
    print("\n_____________________\n")

def run_chi2(df, cat_var, target):
    '''
    This function takes in a pandas DataFrame, a single categorical variable (as a string), and a target variable (as a string). It returns a DataFrame that shows the chi2_summary with observed and expected values.
    '''
    observed = pd.crosstab(df[cat_var], df[target])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    chi2_summary = pd.DataFrame({'variable': [cat_var], 'chi2': [chi2], 'p-value': [p], 
                                 'degrees of freedom': [degf]})
   
    return chi2_summary, observed, expected

def plot_cat_by_target(df, target, cat_var):
    '''
    This function takes in a pandas DataFrame, a single target variable (as a string), and a single categorical variable (as a string). It plots a barplot of the categorical variable, along with line showing the target 
    '''
    p = plt.figure(figsize=(2,2))
    p = sns.barplot(cat_var, target, data=df, alpha=.8, color='lightseagreen')
    overall_rate = df[target].mean()
    p = plt.axhline(overall_rate, ls='--', color='gray')
    return p

def bivariate_metrics(df, target, cat_vars=[]):
    cat_vars, quant_vars = cat_vs_quant(df)
    metric_df = pd.DataFrame({'variable': [], 'chi2': [], 'p-value': [], 
                                 'degrees of freedom': []})  
    for cat in cat_vars:
        observed = pd.crosstab(df[cat], df[target])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        chi2 = chi2.round().astype(int)
        p = p.round(4)
        chi2_summary = pd.DataFrame({'variable': [cat], 'chi2': [chi2], 'p-value': [p], 
                                 'degrees of freedom': [degf]})
        chi2_summary['degrees of freedom'] = chi2_summary['degrees of freedom'].astype(int)
        metric_df = metric_df.append(chi2_summary)
        metric_df = metric_df.sort_values('p-value')
   
      
    return metric_df
#### Bivariate Quantitative

def explore_bivariate_quant(df, target, quant_var):
    '''
    descriptive stats by each target class. 
    compare means across 2 target groups 
    boxenplot of target x quant
    swarmplot of target x quant
    '''
    print(quant_var, "\n____________________\n")
    descriptive_stats = df.groupby(target)[quant_var].describe()
    average = df[quant_var].mean()
    mann_whitney = compare_means(df, target, quant_var)
    plt.figure(figsize=(4,4))
    boxen = plot_boxen(df, target, quant_var)
    swarm = plot_swarm(df, target, quant_var)
    plt.show()
    print(descriptive_stats, "\n")
    print("\nMann-Whitney Test:\n", mann_whitney)
    print("\n____________________\n")

def plot_swarm(df, target, quant_var):
    average = df[quant_var].mean()
    p = sns.swarmplot(data=df, x=target, y=quant_var, color='lightgray')
    p = plt.title(quant_var)
    p = plt.axhline(average, ls='--', color='black')
    return p

def plot_boxen(df, target, quant_var):
    average = df[quant_var].mean()
    p = sns.boxenplot(data=df, x=target, y=quant_var, color='lightseagreen')
    p = plt.title(quant_var)
    p = plt.axhline(average, ls='--', color='black')
    return p

# alt_hyp = ‘two-sided’, ‘less’, ‘greater’

def compare_means(df, target, quant_var, alt_hyp='two-sided'):
    x = df[df[target]==0][quant_var]
    y = df[df[target]==1][quant_var]
    return stats.mannwhitneyu(x, y, use_continuity=True, alternative=alt_hyp)

######################### Multivariate #######################################
################ Can only be done on train ###################################

def plot_all_continuous_vars(df, target, quant_vars):
    '''
    Melt the dataset to "long-form" representation
    boxenplot of measurement x value with color representing target. 
    '''
    my_vars = [item for sublist in [quant_vars, [target]] for item in sublist]
    sns.set(style="whitegrid", palette="muted")
    melt = df[my_vars].melt(id_vars=target, var_name="measurement")
    plt.figure(figsize=(8,6))
    p = sns.boxenplot(x="measurement", y="value", hue=target, data=melt)
    p.set(yscale="log", xlabel='')    
    plt.show()

def plot_violin_grid_with_color(df, target, cat_vars, quant_vars):
    cols = len(cat_vars)
    for quant in quant_vars:
        _, ax = plt.subplots(nrows=1, ncols=cols, figsize=(16, 4), sharey=True)
        for i, cat in enumerate(cat_vars):
            sns.violinplot(x=cat, y=quant, data=df, split=True, 
                           ax=ax[i], hue=target, palette="Set2")
            ax[i].set_xlabel('')
            ax[i].set_ylabel(quant)
            ax[i].set_title(cat)
        plt.show()

def plot_swarm_grid_with_color(df, target, cat_vars, quant_vars):
    cols = len(cat_vars)
    for quant in quant_vars:
        _, ax = plt.subplots(nrows=1, ncols=cols, figsize=(16, 4), sharey=True)
        for i, cat in enumerate(cat_vars):
            sns.swarmplot(x=cat, y=quant, data=df, ax=ax[i], hue=target, palette="Set2")
            ax[i].set_xlabel('')
            ax[i].set_ylabel(quant)
            ax[i].set_title(cat)
        plt.show()

