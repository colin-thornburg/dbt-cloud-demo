import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    words_df = dbt.source('words_seed', 'words')
    words = words_df.values.tolist()
    df = words[:10]
    return df