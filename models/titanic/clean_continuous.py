import pandas as pd
from sklearn.model_selection import train_test_split


def model(dbt, session):
    dbt.config(
        packages = ["scikit-learn", "pandas"],
        materialized="table")
    titanic = dbt.source("titanic_seed", "titanic").to_pandas()

    # Replace null ages with mean
    titanic['AGE'].fillna(titanic['AGE'].mean(), inplace=True)

    # Combine these 2 features together since they are highly correlated
    titanic['Family_cnt'] = titanic['SIBSP'] + titanic['PARCH']

    # Drop features that are not important (do this analysis in notebook)
    titanic.drop(['PASSENGERID', 'SIBSP', 'PARCH'], axis=1, inplace=True)

    return titanic