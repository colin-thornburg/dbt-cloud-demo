import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    #words_df = dbt.source('words_seed', 'words')
    words = []
    for line in open('words.txt', 'r'):
        words.append(line)
    print(len(words))
    df = words[:10]
    return df