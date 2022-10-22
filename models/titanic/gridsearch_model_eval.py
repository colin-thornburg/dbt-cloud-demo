import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from datetime import datetime as dt


def model(dbt, session):
    dbt.config(
        packages = ["scikit-learn"],
        materialized="table")
    titanic = dbt.ref("clean_categorical").to_pandas()
    
    # isolate independent variables (i.e. variables that impact survival)
    features = titanic.drop('SURVIVED', axis=1)

    # isolate dependent variable (i.e. the thing we are trying to predict)
    labels = titanic['SURVIVED']

    # Break data up initially to 60% training, 40% testing
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.4, random_state=42)

    # Break testing set down further --> 20% for testing, 20% for validation --> Training 60%, Testing 20%, Validation 20%
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test,test_size=0.5, random_state=42)

    # Cross Validation
    ## We do this to prevent overfitting.  It's using a different test set for each iteration which in this case is 5 (see cv=5 below)
    rf = RandomForestClassifier()

    scores = cross_val_score(rf, features, labels, cv=5)
    #df = pd.DataFrame(scores, columns = ['Scores'])

    parameters = {
        'n_estimators': [5, 50, 100],
        'max_depth': [2, 10, 20, None]
    }

    cv = GridSearchCV(rf, parameters, cv=5)
    cv.fit(features, labels)

    # Build results
    means_df = pd.DataFrame(cv.cv_results_['mean_test_score'], columns = ['accuracy']) # Returns accuracy
    std_df = pd.DataFrame(cv.cv_results_['std_test_score'], columns = ['std_deviation']) # Returns standard deviation
    params_df = pd.DataFrame(cv.cv_results_['params']) # Returns model complexity parameters
    results_df = pd.concat([means_df, std_df, params_df,], axis=1)
    
    # Add Timestamps
    now = dt.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    results_df['date_time'] = timestamp


    return results_df