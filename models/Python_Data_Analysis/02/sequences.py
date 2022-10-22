import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    nephews = ["Huey", "Dewey", "Louie"]
    df = pd.DataFrame(nephews, columns = ['nephews'])
    return df


    # nephews = ["Huey", "Dewey", "Louie"]
    # for i in range(3):
    #     nephews[i] = nephews[i] + ' Duck'
    # nephews.append('April Duck')
    # df = pd.DataFrame(nephews, columns = ['nephews'])
    # return df


    # nephews.append('April Duck')
    # df = pd.DataFrame(nephews, columns = ['nephews'])
    # return df

    # nephews.extend(['May Duck', 'June Duck'])
    # df = pd.DataFrame(nephews, columns = ['nephews'])
    # return df

    