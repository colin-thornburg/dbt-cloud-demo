import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")


    ###--- Comprehension ^2 each number from 1 to 10 ---###
    squares = [i**2 for i in range(1,11)]
    df = pd.DataFrame(squares,columns=['squares_from_comprehension'])
    return df

    ###--- Comprehension with conditional ---###
    # squares_by_four = [i**2 for i in range(1, 11) if i**2 % 4 == 0]
    # df = pd.DataFrame(squares,columns=['divisible_by_four'])
    # return df

    ###--- Dictionary Comprehension ---###
    # squares_dict = {i: i**2 for i in range(1, 11)}
    # df = pd.DataFrame.from_dict(squares_dict, orient='index',columns=['squared_values'])
    # return df


    ###--- Dictionary Comprehension ---###
    # capitals_by_country = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
    # countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}
    # df = pd.DataFrame.from_dict(countries_by_capital, orient='index',columns=['country'])
    # df = df.rename_axis('capital').reset_index()
    # return df


    ###--- Nested Comprehension ---###
    # counting = [j for i in range(1, 11) for j in range(1, i + 1)]
    # df = pd.DataFrame(counting, columns=['column_name'])
    # return df
    

        