import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def model(dbt, session):
    dbt.config(
        packages = ["scikit-learn"],
        materialized="table")
    titanic = dbt.ref("clean_continuous").to_pandas()

    # if missing, return 0, else 1
    titanic['CABIN_IND'] = np.where(titanic['CABIN'].isnull(), 0, 1) 

    #Convert sex to numeric
    gender_num = {'male': 0, 'female': 1}
    titanic['SEX'] = titanic['SEX'].map(gender_num)

    #Drop unnecessary variables
    titanic.drop(['CABIN', 'EMBARKED', 'NAME', 'TICKET'], axis=1, inplace=True)
    
    return titanic