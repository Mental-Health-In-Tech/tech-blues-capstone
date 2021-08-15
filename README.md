![image](https://github.com/lupeluna/README_FILES/blob/main/Tech%20Blues%20Mental%20Health%20in%20Tech.gif)

# Tech Blues: Improving Mental Health in Tech


Hello,

Welcome to the README file for our Mental Health in Tech Capstone Project.

Here, you will be able to find our project-planning though [Trello](https://trello.com/b/YET89ocX/mental-health-in-tech)



## A. Project Overview
---

### 1. Project Description
We will be the Classification model to see if we can predict whether or not mental health interferes with workplace of tech employees.  
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
Our goal is to be able to succesfully acquire the data, and follow through with the data science pipeline to create a classification model that will predict XXXX, with a better accuracy than XXXX% (the baseline accuracy for assuming whether or not the other factors interfere with work.)
<br>
<br>

### 2.) Initial Thoughts & Hypothesis
> - **Hypothesis 1 -** 
> - (hypothesis between) XXXX - two comparisons go here
> - alpha = .05
> - $H_o$: There is no difference XXXX
> - $H_a$: There is a difference XXXX

> - **Hypothesis 2 -** 
> - (hypothesis between) XXXX - two comparisons go here
> - alpha = .05
> - $H_o$: There is no difference XXXX
> - $H_a$: There is a difference XXXX


We also hope to find XXXX. 


### 3.) Findings & Next Steps

We found that our XXX model performed the best with a:
 - XXXX % score on accuracy
 - XXXX % score on precision
 - XXXX % score on recall
 
It does well with XXXX.
With more time, we should XXXX. 



## C. Data Context
--- 
### 1. About Our Data

Our data was acquired through Kaggle.com. We XXXX. 
<br>


### 2. Data Dictionary

|   Feature       | Description    | Encoding |
| :------------- | ----------- | -----------: |
| timestamp	|  Time survey was submitted | - |
| age	| Respondent age  | - |
| gender	| Respondent gender | male:0, female:1, other:2 |
| country	 |  Respondent survey  | - |
| self_employed	 | Whether or not they were self employed | No:0, Yes:1 |
| family_history	| Whether or not they have a family history of mental illness | No:0, Yes:1 |
| treatment	 |  Whether or not they have sought treatment  | No:0, Yes:1 |
|  work_interfere	  |  If the person felt that the mental condition interfered with work | Never:0, Rarely:1, Sometimes:2, Often:3, NA:4 |
| no_employees	| The number of employees in the company or organization  | <5:0, 6-25:1, 26-100:2, 101-500:3, 501-1000:4, >1000:5 |
| remote_work	 | Having remote work (outside of an office) at least 50% of the time | No:0, Yes:1 |
| tech_company	| The employer is primarily a tech company/organization | No:0, Yes:1 |
| benefits  |	Providing mental health benefits by the employer | No:0, Yes:1, Don't know:2 |
| care_options |	Providing options for mental health care by the employer | No:0, Yes:1, Not sure:2 |
| wellness_program	| Discussion about mental health as part of an employee wellness program by the employees | No:0, Yes:1, Don't know:2 |
| seek_help	| Provided resources by the employer to learn more about mental health issues and how to seek help | No:0, Yes:1, Don't know:2 |
| anonymity |	Protecting anonymity if you choose to take advantage of mental health or substance abuse treatment resources | No:0, Yes:1, Don't know:2 |
| leave  |	How easy is it for you to take medical leave for a mental health condition? | Very difficult:0, Somewhat difficult:1, Don't know:2, Somewhat easy:3, Very easy:4 |
| mental-health_consequence |	Having negative consequences caused by discussing a mental health issue with your employer | No:0, Yes:1, Maybe:2 |
| phys-health_consequence	 | Having negative consequences caused by discussing a physical health issue with your employer  | No:0, Yes:1, Maybe:2 |
| coworkers |	Would you be willing to discuss a mental health issue with your coworkers? | No:0, Yes:1, Some of them:2 |
| supervisor	| Would you be willing to discuss a mental health issue with your direct supervisor(s)? | No:0, Yes:1, Some of them:2 |
| mental_health_interview  |	Would you bring up a mental health issue with a potential employer in an interview?  | No:0, Yes:1, Maybe:2 |
| phys_health_interview |	Would you bring up a physical health issue with a potential employer in an interview?  | No:0, Yes:1, Maybe:2 |
| mental_vs_physical |	Do you feel that your employer takes mental health as seriously as physical health? | No:0, Yes:1, Don't know:2 |
|  obs_consequence  |  Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?  | No:0, Yes:1 |


* Target variable

## D. Pipeline
--- 

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### 1. Project Planning
At a quick glance, the following is what needs to be done: 


##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals
- [x] Acquire data - XXXX. 
- [x] XXXX Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion(s).
- [x]  Clearly define XXXX hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train XXXX different models.
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
> - Clean our data: XXXX
> - Store functions needed to prepare the data
> - Import the prepare/wrangle functions created by using prepare.py or wrangel.py
> - Split the data into train, validate, and test sets


#### 4. Data Exploration
> - Explore the train data.
> - XXXX
> - XXXX 
> - XXXX
> - XXXX
> - Visualize! 


#### 5. Modeling & Evaluation
> - Establish a baseline accuracy 
> - XXX Fit using TD-IDF Vectorizer
> - XXX Evaluate decision tree, random forest, logistic regression, KNN, and Naive Bayes models
> - Emphasize on beating the baseline accuracy, and overall accuracy of the model. 

Here is a quick summary of our results:



| Model               | Train Score | Validate Score | Test Score |
|---------------------|-------------|----------------|------------|
| Decision Tree       | XXXX %      | XXXX %         | ---        |
| Random Forest       | XXXX %      | XXXX %         | ---        |
| Logistic Regression | XXXX %      | XXXX %         | ---        |
| Naive Bayes         | XXXX %      | XXXX %         | ---        |
| KNN                 | XXXX %      | XXXX %         | ---        |






#### 6. Product Delivery
> - Deliver the findings in a Google Slide presentation.
> - Have a completed final notebook with comments to explain the walkthrough of our process
> - Acquire, prepare, and explore .py files completed with docstrings and used in our notebook
> - Completed README for project information (summary, pipeline, findings and next steps, etc.)

<br>
<br>

## E.) Modules
---
- acquire.py = contains data acquisiton functions used to scrape the data, as well as to bring it in from our local server
- prepare.py = contains preparation functions to filter and clean our data
- explore.py = contains explore functions that will generate visualizations 




## F. Project Reproduction
--- 


You will need your own env file with database credentials along with all the necessary files listed below to run our final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and NLP_df.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_nlp.ipynb notebook
