import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV


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
    df = pd.DataFrame(scores, columns = ['Scores'])
    return df