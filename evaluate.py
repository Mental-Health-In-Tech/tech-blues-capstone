import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression, chi2
import time
import matplotlib.pyplot as plt

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

def run_metrics(X, y, model, data_set = 'This'):
    """
    Takes in X , target as y, the model for testing, and the data_set(i.e. train, validate, test)\n
    Outputs a print list with the confusion matrix, classification report, confusion matrix, and the T/F +/- rate
    """
    score = model.score(X, y)
    matrix = confusion_matrix(y, model.predict(X))
    tpr = matrix[1,1] / (matrix[1,1] + matrix[1,0])
    fpr = matrix[0,1] / (matrix[0,1] + matrix[0,0])
    tnr = matrix[0,0] / (matrix[0,0] + matrix[0,1])
    fnr = matrix[1,0] / (matrix[1,1] + matrix[1,0])
    prc = matrix[1,1] / (matrix[1,1] + matrix[0,1])
    
    print(f'{data_set} data set accuracy score: {score:.2%}')
    print(f'{data_set} data set precision score {prc:.2%}')
    print(f'{data_set} data set recall score: {tpr:.2%}\n')
    class_report = classification_report(y, model.predict(X), zero_division=True)
    print('-------------------------------')
    print(f'classification report')
    print(class_report)
    print ('-------------------------------\n')
    print('confusion matrix')
    print(f'{matrix}\n')
    print(f'{data_set} data set model metrics')
    print('---------------------------------')
    print(f'True positive rate for the model is {tpr:.2%}')
    print(f'False positive rate for the model is  {fpr:.2%}')
    print(f'True negative rate for the model is {tnr:.2%}')
    print(f'False negative rate for the model is {fnr:.2%}\n')
    
def select_kbest(X, y, stats = f_regression, k = 3):
    '''select_kbest(X, y, stats = f_regression, k = 3)
    can change stats test to chi2 if working with categorical variables.
    k is default to 3, but can be edited to give more features.
    returns a list of k best features '''
    X_best= SelectKBest(stats, k).fit(X, y)
    mask = X_best.get_support() #list of booleans for selected features
    new_feat = [] 
    for bool, feature in zip(mask, X.columns):
        if bool:
            new_feat.append(feature)
    return print('The best features are:{}'.format(new_feat))

def get_importances(model):
    '''This function takes in a tree based model and returns an array 
       of feature weights and the standard deviation between each tree
       in the forest'''
    # get start time
    start_time = time.time()
    # pull out feature importances
    importances = model.feature_importances_
    # find the standard deviation of feature importances for each tree in the random forest
    std = np.std([
        x.feature_importances_ for x in model.estimators_], axis=0)
    # calculate the elapsed time for analysis
    elapsed_time = time.time() - start_time
    print(f"Elapsed time to compute the importances: "
          f"{elapsed_time:.3f} seconds")
    return importances, std

def graph_importances(data, importances, std): 
    '''Takes in the X_train for data, array of feature importance, and
       standard deviation of estimators in the forest. Returns a graph
       plotting mean decrease in impurity for each feature'''
    # create feature names for x label of the chart
    feature_names = [f'feature {i}' for i in range(data.shape[1])]
    # get importances for each feature
    forest_importances = pd.Series(importances, index=feature_names)
    fig, ax = plt.subplots()
    # Use std for errorbars, place each feautre importance on the chart
    forest_importances.plot.bar(yerr=std, ax=ax)
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20, pad = 5)
    ax.set_title("Feature importances using MDI")
    ax.set_ylabel("Mean decrease in impurity")
    return fig.tight_layout()