'''
Data Acquisition ->
Data Cleaning (Pandas) ->
Training Data/ Test Data/ Validation Data ->
Model Training and Building ->
Adjust Model Parameters ->
Deploy Model

1.Evaluating Performance - Classification Error Metrics / Overfitting
    - Accuracy = Correct Num Predictions / Total Num Predictions
        - not good for unbalanced classes (99 dogs and 1 cat)
    - Recall = true positives / true positives + false negatives
        - the ability of a model to find all the relevant cases within a dataset
    - Precision = true positives / true positives + false positives
        - the ability of a classification model to identify only the relevant data points
    - F1-Score = 2 * (precision * recall) / (precision + recall)
        - in cases we want to find an optimal blend of precision and recall we can combine the 2 metrics


    - Confusion matrix

2.Evaluating Performance - Regression Error Metrics
    - mean absolute error (MAE) = |true value - predicted value|
    - mean squared error (MST) = |true value - predicted value|**2
    - root mean squared error (RMSE)

3. Scikit Learn package:
    pip install scikit-learn
'''
#LINEAR REGRESSION
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# %matplotlib inline
df = pd.read_csv('USA_Housing.csv')
print(df.head())
print(df.info())
print(df.describe())
# print(df.columns())
print(sns.distplot(df['Price']))

