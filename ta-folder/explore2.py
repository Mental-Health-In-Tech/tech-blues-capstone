# Tech Blues Capstone Explore Module

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split


############################ Split The Data ##################################

def three_split(df, target, seed=123):
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

########################## Univariate Exploration #############################################

########## Mother Function

def mental_health_univariate(df):
    '''
    This function takes in a pandas DataFrame, and performs univariate analysis for each variable.
    - Categorical variables will return a countplot
    - Continuous variables will return a histogram, and boxplot
    '''
    cat_vars, quant_vars = cat_vs_quant(df)
    
    
    for cat in cat_vars:
        plt.figure(figsize=(4, 4))
        sns.countplot(df[cat])
        
        plt.show()
        
    for quant in quant_vars:
        plt.figure(figsize=(12, 4))
        plot_univariate_quant(df)
        
####### Categorical Variables


####### Continuous Variables

def plot_univariate_quant(df):
    '''
    This function takes in a pandas DataFrame, creates a list of continuous variables, and plots histograms, and boxplots of the variables.
    '''
    
    cat_vars, quant_vars = cat_vs_quant(df)
    
    for quant in quant_vars:
        plt.subplot(1, 2, 1)
        sns.histplot(data = df, x = df[quant], kde=True)
        plt.title(f'{quant} distribution')
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[quant], data=df)
        plt.title(f'{quant} distribution')
        plt.show()  
        
################################ Bivariate Functions #############################################

############### Mother Function

def mental_health_bivariate(df, target, cat_vars=[], quant_vars=[]):
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
        bivariate_categorical(df, target, cat)
    for quant in quant_vars:
        bivariate_quant(df, target, quant)
    mets = bivariate_metrics(df, target, cat_vars=[]) 
    print(mets)
    return mets

################## Categorical Variables

def bivariate_categorical(df, target, cat_var):
    '''
    This function takes in pandas DataFrame, a target variable (as a string) and a single categorical variable (as a string). It runs a chi-square test for the proportions and creates a barplot, adding a horizontal line of the overall rate of the target. 
    '''
    
    ct = pd.crosstab(df[cat_var], df[target], margins=True)
    chi2_summary, observed, expected = run_chi2(df, cat_var, target)
    p = plot_cat_by_target(df, target, cat_var)

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
    p = plt.figure(figsize=(4,4))
    p = plt.rcParams.update({'font.size': 12})
    p = plt.title(f'{cat_var} & work_interfere')
    p = sns.barplot(cat_var, target, data=df, alpha=.8)
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
        chi2 = float('{:.2f}'.format(chi2))
        p = float('{:.4f}'.format(p))
        chi2_summary = pd.DataFrame({'variable': [cat], 'chi2': [chi2], 'p-value': [p], 
                                 'degrees of freedom': [degf]})
        chi2_summary['degrees of freedom'] = chi2_summary['degrees of freedom'].astype(int)
        metric_df = metric_df.append(chi2_summary)
        metric_df = metric_df.sort_values('p-value').reset_index(drop=True)
    
    return metric_df

################ Continuous Variables

def bivariate_quant(df, target, quant_var):
    '''
    descriptive stats by each target class. 
    compare means across 2 target groups 
    boxenplot of target x quant
    swarmplot of target x quant
    '''
    print(quant_var)
    descriptive_stats = df.groupby(target)[quant_var].describe()
    average = df[quant_var].mean()
    mann_whitney = compare_means(df, target, quant_var)
    plt.figure(figsize=(8,4))
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
    p = sns.boxenplot(data=df, x=target, y=quant_var)
    p = plt.title(quant_var)
    p = plt.axhline(average, ls='--', color='black')
    return p

# alt_hyp = ‘two-sided’, ‘less’, ‘greater’

def compare_means(df, target, quant_var, alt_hyp='two-sided'):
    x = df[df[target]==0][quant_var]
    y = df[df[target]==1][quant_var]
    return stats.mannwhitneyu(x, y, use_continuity=True, alternative=alt_hyp)
    
################ Splitting Variables Categorical vs Continuous

def cat_vs_quant(df):
    '''
    This function takes in a pandas DataFrame, and returns lists of categorical and quantitative variables.
    '''
    
    cat_vars = []
    quant_vars = ['age']
    col_list = list(df.columns)
    
    for col in col_list:
        if df[col].nunique()<=6:
            cat_vars.append(col)
#         else:
#             no_need.append(col)
    
    return cat_vars, quant_vars



######################### One-Hot Encoding #######################################

def one_hot(encoded_df):
    '''
    One-hot encoding all categorical variables that have more than two unique observations.
    '''
    
    selected_cols_df = encoded_df[['gender', 'work_interfere', 'company_size', 'leave', 'care_options', 'benefits', 'wellness_program', 'seek_help', 'anonymity', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical']]
    
    encoded_dummies = pd.get_dummies(data=selected_cols_df, columns = ['gender', 'company_size', 'leave', 'care_options', 'benefits', 'wellness_program', 'seek_help', 'anonymity', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical'])
    
    new_df = pd.concat([encoded_df['age'], encoded_dummies], axis=1)
    
    return new_df

def two_hot(encoded_df):
    '''
    One-hot encoding all categorical variables that have more than two unique observations.
    '''
    
    selected_cols_df = encoded_df[['gender', 'work_interfere', 'company_size', 'leave', 'care_options', 'benefits', 'wellness_program', 'seek_help', 'anonymity', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical']]
    
    encoded_dummies = pd.get_dummies(data=selected_cols_df, columns = ['gender', 'company_size', 'leave', 'care_options', 'benefits', 'wellness_program', 'seek_help', 'anonymity', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical'], drop_first=True)
    
    new_df = pd.concat([encoded_df['age'], encoded_dummies], axis=1)
    
    return new_df

################### Hypothesis Testing ##########################################

def ty_chi(df, target, col_2):
    '''
    This function takes in a pandas dataframe, along with two columns. 
    It runs a chi2_contingency on the two columns and prints out the column names, chi2 score, and p-value.
    '''
    # create a crosstab of the variables being tested
    observed = pd.crosstab(df[target], df[col_2])
    # run chi^2 testing on crosstab
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    print(f'{target} & {col_2} chi2 test results')
    print('')
    print(f'chi^2 = {chi2:.2f}')
    print(f'    p = {p:.4f}')
    
def three_chi(df, control, target, col_2):
    '''
    This function takes in a pandas DataFrame, a control variable, target_variable, and other variable.
    It creates separate DataFrames that control for the control variable.
    '''
    length = len(df[control].value_counts())
    span = range(0,length)
    
    for i in span:
        sub_df = df[df[control]==i]
        observed = pd.crosstab(sub_df[target], sub_df[col_2])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        print(f'controlling for {control} = {i}')
        print('')
        print(f'{target} & {col_2} chi2 test results')
        print('')
        print(f'chi^2 = {chi2:.2f}')
        print(f'    p = {p:.4f}')
        print('')
        print('-----------------------------------')

# ######################## Mother Functions ######################################

# def explore_univariate(df, cat_vars=[], quant_vars=[]):
#     '''
#     This function takes in a pandas DataFrame, a list of categorical variables, and a list of quantitative variables.
#     It uses the 'explore_univariate_categorical' and 'explore_univariate_quantitative' functions to plot:
#     - frequency tables and barplots for categorical data,
#     - descriptive stats, histograms, and boxplots for quantitative variables.
#     '''
#     cat_vars, quant_vars = cat_vs_quant(df)
    
#     for cat in cat_vars:
#         explore_univariate_categorical(df, cat)
#         print('_________________________________________________________________')
#     for quant in quant_vars:
#         p, descriptive_stats = explore_univariate_quant(df, quant)
#         plt.show(p)
#         print(descriptive_stats)
        
# def explore_bivariate(df, target, cat_vars=[], quant_vars=[]):
#     '''
#     This function takes in a pandas DataFrame, a target variable (as a string), a list of categorical variables,
#     and a list of quntitative variables. It opperates on top of the 'explore_bivarite_categorical' and 
#     'explore_bivariate_quantitative' functions to return:
#     - categorical variables:
#         - 
#     - quantitative variables:
#         - 
#     '''
#     cat_vars, quant_vars = cat_vs_quant(df)
    
#     for cat in cat_vars:
#         explore_bivariate_categorical(df, target, cat)
#     for quant in quant_vars:
#         explore_bivariate_quant(df, target, quant)

# def explore_multivariate(df, target, cat_vars=[], quant_vars=[]):
#     '''
#     '''

#     print('printing swarmgrid...')
#     plot_swarm_grid_with_color(df, target, cat_vars, quant_vars)
#     plt.show()
#     print('making violin...')
#     violin = plot_violin_grid_with_color(df, target, cat_vars, quant_vars)
#     plt.show()
#     print('making pairplot...')
#     pair = sns.pairplot(data=df, vars=quant_vars, hue= target)
#     plt.show()
#     print('plotting continuous vars')
#     plot_all_continuous_vars(df, target, quant_vars)
#     plt.show()  
    
# ########################## Univariate #########################################
# ########### Can be done on entire dataset, or train ###########################
        
# def explore_univariate_categorical(df, cat_var):
#     '''
#     This function takes in a pandas DataFrame, and a single categorical variable in the dataset,
#     and returns a frequency table and barplot of the categorical variable.
#     '''
    
#     # makes the frequency table
#     frequency_table = freq_table(df, cat_var)
#     # sets the figure size for the barplot
#     plt.figure(figsize=(4,4))
#     # creates the barplot, ***color needs to be changed***
#     sns.barplot(x=cat_var, y='Count', data=frequency_table, color='lightseagreen')
#     # sets the title of the barplot based on the categorical variable
#     plt.title(f'{cat_var} Bar Plot in Mental Heath Data')
#     # shows the barplot
#     plt.show()
#     # prints the frequency table
#     print(frequency_table)
    
# def explore_univariate_quant(df, quant_var):
#     '''
#     This function takes in a pandas DataFrame, and a single quantitative variable, and returns
#     descriptive stats table, histogram, and boxplot of the distributions. 
#     '''
#     # runs the descriptive stats of the quantitative variable
#     descriptive_stats = df[quant_var].describe()
#     # sets the figure size of the plot entire plot
#     plt.figure(figsize=(12,4))
#     # first subplot (top left) us the histogram of quant_var
#     p = plt.subplot(1, 2, 1)
#     # ***** Need to change the color ******************
#     p = plt.hist(df[quant_var], color='lightseagreen')
#     # sets the title for the histogram
#     p = plt.title(f'{quant_var} Histogram in Mental Health Data')

#     # second plot (top right): box plot
#     p = plt.subplot(1, 2, 2)
#     p = plt.boxplot(df[quant_var])
#     # sets the title for the boxplot
#     p = plt.title(f'{quant_var} Boxplot in Mental Health Data')
#     return p, descriptive_stats

# def freq_table(df, cat_var):
#     '''
#     This function takes in a pandas DataFrame, along with a single categorical variable.
#     It computes the frequency count and percent split
#     and return a dataframe of those values along with the different classes. 
#     '''
#     class_labels = list(df[cat_var].unique())

#     frequency_table = (
#         pd.DataFrame({cat_var: class_labels,
#                       'Count': df[cat_var].value_counts(normalize=False), 
#                       'Percent': round(df[cat_var].value_counts(normalize=True)*100,2)}
#                     )
#     )
#     return frequency_table

# ############################ Bivariate Exploration ############################

# ############## This can be only be done on the train dataset ##################

# #### Bivariate Categorical
        
# def explore_bivariate_categorical(df, target, cat_var):
#     '''
#     This function takes in pandas DataFrame, a target variable (as a string) and a single categorical variable (as a string). It runs a chi-square test for the proportions and creates a barplot, adding a horizontal line of the overall rate of the target. 
#     '''
#     print(cat_var, "\n_____________________\n")
#     ct = pd.crosstab(df[cat_var], df[target], margins=True)
#     chi2_summary, observed, expected = run_chi2(df, cat_var, target)
#     p = plot_cat_by_target(df, target, cat_var)

#     print(chi2_summary)
#     print("\nobserved:\n", ct)
#     print("\nexpected:\n", expected)
#     plt.show(p)
#     print("\n_____________________\n")
    

# def run_chi2(df, cat_var, target):
#     '''
#     This function takes in a pandas DataFrame, a single categorical variable (as a string), and a target variable (as a string). It returns a DataFrame that shows the chi2_summary with observed and expected values.
#     '''
#     observed = pd.crosstab(df[cat_var], df[target])
#     chi2, p, degf, expected = stats.chi2_contingency(observed)
#     chi2_summary = pd.DataFrame({'chi2': [chi2], 'p-value': [p], 
#                                  'degrees of freedom': [degf]})
#     expected = pd.DataFrame(expected)
#     return chi2_summary, observed, expected

# def plot_cat_by_target(df, target, cat_var):
#     '''
#     This function takes in a pandas DataFrame, a single target variable (as a string), and a single categorical variable (as a string). It plots a barplot of the categorical variable, along with line showing the target 
#     '''
#     p = plt.figure(figsize=(4,4))
#     p = sns.barplot(cat_var, target, data=df, alpha=.8, color='lightseagreen')
#     overall_rate = df[target].mean()
#     p = plt.axhline(overall_rate, ls='--', color='gray')
#     return p
    
# #### Bivariate Quantitative

# def explore_bivariate_quant(df, target, quant_var):
#     '''
#     descriptive stats by each target class. 
#     compare means across 2 target groups 
#     boxenplot of target x quant
#     swarmplot of target x quant
#     '''
#     print(quant_var, "\n____________________\n")
#     descriptive_stats = df.groupby(target)[quant_var].describe()
#     average = df[quant_var].mean()
#     mann_whitney = compare_means(df, target, quant_var)
#     plt.figure(figsize=(4,4))
#     boxen = plot_boxen(df, target, quant_var)
#     swarm = plot_swarm(df, target, quant_var)
#     plt.show()
#     print(descriptive_stats, "\n")
#     print("\nMann-Whitney Test:\n", mann_whitney)
#     print("\n____________________\n")

# def plot_swarm(df, target, quant_var):
#     average = df[quant_var].mean()
#     p = sns.swarmplot(data=df, x=target, y=quant_var, color='lightgray')
#     p = plt.title(quant_var)
#     p = plt.axhline(average, ls='--', color='black')
#     return p

# def plot_boxen(df, target, quant_var):
#     average = df[quant_var].mean()
#     p = sns.boxenplot(data=df, x=target, y=quant_var, color='lightseagreen')
#     p = plt.title(quant_var)
#     p = plt.axhline(average, ls='--', color='black')
#     return p

# # alt_hyp = ‘two-sided’, ‘less’, ‘greater’

# def compare_means(df, target, quant_var, alt_hyp='two-sided'):
#     x = df[df[target]==0][quant_var]
#     y = df[df[target]==1][quant_var]
#     return stats.mannwhitneyu(x, y, use_continuity=True, alternative=alt_hyp)

# ######################### Multivariate #######################################
# ################ Can only be done on train ###################################

# def plot_all_continuous_vars(df, target, quant_vars):
#     '''
#     Melt the dataset to "long-form" representation
#     boxenplot of measurement x value with color representing target. 
#     '''
#     my_vars = [item for sublist in [quant_vars, [target]] for item in sublist]
#     sns.set(style="whitegrid", palette="muted")
#     melt = df[my_vars].melt(id_vars=target, var_name="measurement")
#     plt.figure(figsize=(8,6))
#     p = sns.boxenplot(x="measurement", y="value", hue=target, data=melt)
#     p.set(yscale="log", xlabel='')    
#     plt.show()

# def plot_violin_grid_with_color(df, target, cat_vars, quant_vars):
#     cols = len(cat_vars)
#     for quant in quant_vars:
#         _, ax = plt.subplots(nrows=1, ncols=cols, figsize=(16, 4), sharey=True)
#         for i, cat in enumerate(cat_vars):
#             sns.violinplot(x=cat, y=quant, data=df, split=True, 
#                            ax=ax[i], hue=target, palette="Set2")
#             ax[i].set_xlabel('')
#             ax[i].set_ylabel(quant)
#             ax[i].set_title(cat)
#         plt.show()

# def plot_swarm_grid_with_color(df, target, cat_vars, quant_vars):
#     cols = len(cat_vars)
#     for quant in quant_vars:
#         _, ax = plt.subplots(nrows=1, ncols=cols, figsize=(16, 4), sharey=True)
#         for i, cat in enumerate(cat_vars):
#             sns.swarmplot(x=cat, y=quant, data=df, ax=ax[i], hue=target, palette="Set2")
#             ax[i].set_xlabel('')
#             ax[i].set_ylabel(quant)
#             ax[i].set_title(cat)
#         plt.show()
