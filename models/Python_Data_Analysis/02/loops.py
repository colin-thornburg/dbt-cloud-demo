import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    list = []
    for i in range(0, 10):
        list.append(i)
    df = pd.DataFrame(list, columns = ['column_list'])
    return df


    # combinations = []

    # for count_100 in range(1+1):
    #     for count_50 in range(2+1):
    #         for count_25 in range(4+1):
    #             for count_10 in range(10+1):
    #                 for count_5 in range(20+1):
    #                     for count_1 in range(100+1):
    #                         if 100*count_100 + 50*count_50 + 25*count_25 + 10*count_10 + 5*count_5 + count_1 == 100:
    #                             combinations.append([count_100, count_50, count_25, count_10, count_5, count_1])

    # df = pd.DataFrame(combinations)
    # # column names must be string values
    # df = df.rename(columns={0: 'Zero', 1 : 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'})
    # return df
