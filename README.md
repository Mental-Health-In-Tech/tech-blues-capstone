![image](https://github.com/lupeluna/README_FILES/blob/main/Tech%20Blues%20Mental%20Health%20in%20Tech.gif)

# Tech Blues: Improving Mental Health in Tech


Hello,

Welcome to the README file for our Mental Health in Tech Capstone Project.

Here, you will be able to find our project-planning though [Trello](https://trello.com/b/YET89ocX/mental-health-in-tech)



## A. Project Overview
---

### 1. Project Description
We will be using a Classification model to see if we can predict the drivers of mental health and whether or not they interfere with tech employees in the workplace.  
<br>
<br>


### 2. Project Deliverables
 - Acquire, Prepare, and Explore Modules
 - Final Notebook (a walkthrough with comments)
 - Presentation Slides 
 - This README 
<br>
<br>


## B. Project Summary
---

### 1. Goals  
Our goal is to be able to succesfully acquire the data, and follow through with the data science pipeline to create a classification model that will predict the drivers of mental health in the tech workplace, with a better accuracy than 63% (the baseline accuracy for assuming whether or not the other factors interfere with work.)
<br>
<br>

### 2.) Initial Thoughts & Hypothesis

> Hypothesis 1: 'Supervisor'
> - alpha : 0.05
> - ${H_0}$: The mean workplace interference is the same for those who feel comfortable speaking with their supervisor about mental health issues, and those who do not feel comfortable.
> - ${H_a}$: The mean workplace interference is different for those who feel comfortable speaking with their supervisor about mental health issues than those who do not feel comfortable communicating those issues with their supervisor.

#### Hypothesis 1 - Key Findings, Takeaways, and Next Steps:
- 'Supervisor'
- Since the p-value is less than alpha, we can reject the null hypothesis. There is evidence to suggest a relationship between an employee feeling comfortable speaking with a supervisor about personal mental health issues and work interference.

> Hypothesis 2: Does having benefits affect whether or not you seek treatment affect work interference?
> - alpha : 0.05
> - ${H_0}$: There is no difference between having benefits and whether or not treatment is sought.
> - ${H_a}$: There is a difference between having benefits and whether or not treatment is sought.

#### Hypothesis 2 - Key Findings, Takeaways, and Next Steps:
- Due to our p-value being less than alpha, we reject the null hypothesis.
- There is evidence to suggest a relationship between individuals who have sought treatment in the past and whether or not they have benefits affects work interference.

> Hypothesis 3: If you have observed negative consequences for coworkers with mental health conditions do you not talk to your supervisor and this interferes with your work performance?
> - alpha : 0.05
> - ${H_0}$: There is no difference between observed negative consequences for coworkers with mental health conditions and talking to my supervisor.
> - ${H_a}$: There is a difference between observed negative consequences for coworkers with mental health conditions and talking to my supervisor.

#### Hypothesis 3 - Key Findings, Takeaways, and Next Steps:
- Due to our p-value being less than alpha, we reject the null hypothesis for employees who are able to speak to some of their supervisors about mental health. 
- Due to our p-value being more than alpha for supervisor option 0 (No can't speak to supervisor) and option 1 (yes they can speak to their supervisor), we fail to reject the null hypothesis.
- The only relevant relationship here after assessing the p-value is for employees who are able to speak to some of their supervisors about mental health and who have or have not observed/heard of negative consequences for coworkers with mental health conditions. It seems this group is more than 50% likely to experience work interference.

> Hypothesis 4: If you believe speaking about mental health has negative consequences have/have not sought treatment to the point where it interferes with work?
> - alpha : 0.05
> - ${H_0}$: If you believe speaking about mental health has negative consequences and have/have not sought it has no affect with work interference?
> - ${H_a}$: If you believe speaking about mental health has negative consequences and have/have not sought it has an affect with work interference?

#### Hypothesis 4 - Key Findings, Takeaways, and Next Steps:
- Due to our p-value being less than alpha, we reject the null hypothesis except for mental health consequence option 2 (Maybe).
- Due to our p-value being more than alpha, we fail to reject the null hypothesis except for mental health consequence option 0 (No) and option 1 (Yes).
- The only relationship we can look at here due to the p-values is for the group of employees who are unsure if speaking with their employer about mental health would have negative consequences.
- For employees who are unsure if there will be negative consequences speaking about mental health to their employer and has not observed any negative consequences they have higher than a 50% increase in work interference. 

> Hypothesis 5: 'Supervisor'
> - alpha : 0.05
> - ${H_0}$: The mean workplace interference is the same for those who feel comfortable speaking with their supervisor about mental health issues, and those who do not feel comfortable.
> - ${H_a}$: The mean workplace interference is different for those who feel comfortable speaking with their supervisor about mental health issues than those who do not feel comfortable communicating those issues with their supervisor.

#### Hypothesis 5 - Key Findings, Takeaways, and Next Steps:
- Due to our p-value being less than alpha, we reject the null hypothesis.
- There is evidence to suggest a relationship between feeling comfortable speaking with a supervisor about personal mental health issues and our target variable, 'work_interfere'

> Hypothesis 6: controlling for `gender`, how does `talking to a supervisor` relate to `work_interfere`
> - alpha : 0.05
> - ${H_0}$: When controlling for gender, the rate of work interference is the same among all responses to mental_vs_physical
> - ${H_a}$: When controlling for gender, the rate of work interference is different among each response to mental_vs_physical

#### Hypothesis 6 - Key Findings, Takeaways, and Next Steps:
- Men who feel comfortable speaking about mental health issues with a supervisor have work place interference at a significantly lower rate than those who either feel uncomfortable, or do not know.
- For women, it surprisingly does not seem to matter how they responded to the 'supervisor' question
- There is not enough data for gender=other to have actionable insight
- We recommend that companies work to improve communication between management and staff, as there is clear evidence that it greatly helps reduce the rate of workplace interference amongst men, and does not harm anyone else.

> Hypothesis 7: controlling for `gender`, how does `mental_vs_physical` relate to `work_interfere`
> - alpha : 0.05
> - ${H_0}$: When controlling for gender, the rate of work interference is the same among all responses to mental_vs_physical
> - ${H_a}$: When controlling for gender, the rate of work interference is different among each response to mental_vs_physical

#### Hypothesis 7 - Key Findings, Takeaways, and Next Steps:
- Men who feel that their company takes mental health as seriously as physical health have work interference at a significantly lower rate than those who do not, or do not know.
- Women who feel that their company takes mental health as seriously as physical health have work interference at a lower rate than those who do not, or do not know.
- Once again, we do not have enough data where gender = other to have actionable insight.
We also hope to find XXXX. 


### 3.) Findings & Next Steps

We found that our RandomForestClassifier performed the best predicting for work interference:
 - Baseline accuracy: 63.11 %
 - Train data set: 
     - accuracy score: 88.31%
     - precision score 94.20%
     - recall score: 81.66%
 - Validation set:
     - accuracy score: 83.04%
     - validate data set precision score 94.92%
     - validate data set recall score: 77.24%
 - Test set
     - 85.94% accuracy score
     - 93.52% precision score
     - 83.47% recall score  



## C. Data Context
--- 
### 1. About Our Data

Our data was acquired through [Kaggle](https://www.kaggle.com/osmi/mental-health-in-tech-survey).  It is a dataset from a 2014 survey that measures attitudes towards mental health and frequency of mental health disorders in the tech workplace. 
<br>


### 2. Data Dictionary

|   Feature       | Description    | Encoding |
| :------------- | ----------- | -----------: |
| timestamp	|  Time survey was submitted | - |
| age	| Respondent age  | - |
| gender	| Respondent gender | male:0, female:1, other:2 |
| country	 |  Respondent survey  | - |
| self_employed	 | Are you self-employed? | No:0, Yes:1 |
| family_history	| Do you have a family history of mental illness? | No:0, Yes:1 |
| treatment	 |  Have you sought treatment for a mental health condition?  | No:0, Yes:1 |
|  work_interfere	*  |  If you have a mental health condition, do you feel that it interferes with your work? | Never:0, Rarely:1, Sometimes:2, Often:3, NA:4 |
| no_employees	| How many employees does your company or organization have?  | <5:0, 6-25:1, 26-100:2, 101-500:3, 501-1000:4, >1000:5 |
| remote_work	 | Do you work remotely (outside of an office) at least 50% of the time? | No:0, Yes:1 |
| tech_company	| Is your employer primarily a tech company/organization? | No:0, Yes:1 |
| benefits  |	Does your employer provide mental health benefits? | No:0, Yes:1, Don't know:2 |
| care_options |	Do you know the options for mental health care your employer provides? | No:0, Yes:1, Not sure:2 |
| wellness_program	| Has your employer ever discussed mental health as part of an employee wellness program? | No:0, Yes:1, Don't know:2 |
| seek_help	| Does your employer provide resources to learn more about mental health issues and how to seek help? | No:0, Yes:1, Don't know:2 |
| anonymity |	Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources? | No:0, Yes:1, Don't know:2 |
| leave  |	How easy is it for you to take medical leave for a mental health condition? | Very difficult:0, Somewhat difficult:1, Don't know:2, Somewhat easy:3, Very easy:4 |
| mental-health_consequence |	Do you think that discussing a mental health issue with your employer would have negative consequences? | No:0, Yes:1, Maybe:2 |
| phys-health_consequence	 | Do you think that discussing a physical health issue with your employer would have negative consequences?  | No:0, Yes:1, Maybe:2 |
| coworkers |	Would you be willing to discuss a mental health issue with your coworkers? | No:0, Yes:1, Some of them:2 |
| supervisor	| Would you be willing to discuss a mental health issue with your direct supervisor(s)? | No:0, Yes:1, Some of them:2 |
| mental_health_interview  |	Would you bring up a mental health issue with a potential employer in an interview?  | No:0, Yes:1, Maybe:2 |
| phys_health_interview |	Would you bring up a physical health issue with a potential employer in an interview?  | No:0, Yes:1, Maybe:2 |
| mental_vs_physical |	Do you feel that your employer takes mental health as seriously as physical health? | No:0, Yes:1, Don't know:2 |
|  obs_consequence  |  Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?  | No:0, Yes:1 |


> * Target variable

## D. Pipeline
--- 

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### 1. Project Planning
At a quick glance, the following is what needs to be done: 
We are going to download the .csv file ‘Mental Health in Tech Survey’ from [Kaggle](https://www.kaggle.com/osmi/mental-health-in-tech-survey).  Once we download the file, we will filter for desirable variables of mental health that could interfere with work (benefits, family history, gender, etc.). We will then follow the steps of the data science pipeline to setup the information for our slides presentation.


##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals
- [x] Acquire data - We will download the .csv file named 'Mental Health in Tech Survey' from [Kaggle](https://www.kaggle.com/osmi/mental-health-in-tech-survey). 
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in the prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion(s).
- [x]  Clearly define 8 hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train 4 different models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___



#### 2. Data Acquisition
> - Download survey.csv file into.
> - Save this data locally
> - Store function, in a module, that are needed to acquire the repository and survey data from Kaggle.
> - The final function will return a pandas DataFrame for our use


#### 3. Data Preparation
> - Clean our data: keep only the desirable variables of mental health that could interfere with work.
> - Store functions needed to prepare the data
> - Import the prepare/wrangle functions created by using prepare.py or wrangle.py
> - Split the data into train, validate, and test sets


#### 4. Data Exploration
> - Create detail questions we want to ask of the data.
> - Perform univariate analysis on the entire dataset.
> - Perform bivariate and multivariate analysis on the training dataset.
> - Perform statistical testing on each of our initial hypotheses.
> - Use data from initial exploration to determine drivers of workplace interference.
> - Determine key relationships between drivers to see if the data creates any groups not seen at surface level.
> - Document key findings, takeaways, and next steps for each stage of exploration
> - Visualize! 


#### 5. Modeling & Evaluation
> - Establish a baseline accuracy 
> - Evaluate decision tree, random forest classifier, XGBoost, and multi-layer perceptron classifier models
> - Use accuracy to determine if models are better than baseline
> - The model should be best predicting the most costly case, which is employees who's mental health interferes with work. For that reason, evaluate models using f1 score so that false negatives are weighted more heavily. 
> - Use the best model on out-of-sample data.

Here is a quick summary of our results:

Baseline Accuracy : 63%

| Model               | Train Score | Validate Score | Test Score |
|---------------------|-------------|----------------|------------|
| Decision Tree       | 87 %      | 82 %         | ---        |
| Random Forest       | 88 %      |  83%         | 85%        |
| XGBoost             | 95 %      | 80%         | ---        |
| Multi-layer Perceptron | 91 %   | 82 %         | ---        |






#### 6. Product Delivery
> - Deliver the findings in a Canva Slide presentation.
> - Have a completed final notebook with markdowns and comments to explain the walkthrough of our process
> - Acquire, prepare, and wrangle .py files completed with docstrings and used in our notebook
> - Completed README for project information (summary, pipeline, findings and next steps, etc.)

<br>
<br>

## E.) Modules
---
- wrangle.py = contains the acquire function along with the prepare functions which will filter and clean our data
- explore.py =  contains explore functions that will generate visualizations
- evaluate.py = contains the metrics needed for modeling
- imbalance-learn was used to deal with class imbalance
- scikit-learn was used for MLPClassifier, RandomForestClassifier, and DecisionTree
- xgboost was used to fit the XGBoost classifier


## F. Project Reproduction
--- 


- [X] Read this README.md
- [ ] Download the survey.csv file into your working directory
- [ ] Download the aquire.py, prepare.py, wrangle.py and Tech_Blues_Final.ipynb files into your working directory
- [ ] Clone this repo
- [ ] Run the Tech_Blues_Final.ipynb notebook
