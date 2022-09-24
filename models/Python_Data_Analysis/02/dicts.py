import pandas as pd


def model(dbt, session):
    dbt.config(materialized="table")

    ###--- Simple Dictionaries ---###
    capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
    capitals['Spain'] = 'Madrid'
    morecapitals = {'Germany': 'Berlin', 'United Kingdom': 'London'}
    capitals.update(morecapitals)
    df = pd.DataFrame([capitals])
    return df

    ###--- Loop over Dictionary Keys ---###
    # keys_list = []
    # for country in capitals:
    #     keys_list.append(country)
    # df = pd.DataFrame(keys_list, columns = ['countries'])
    # return df

    ###--- Loop over Dictionary Values ---###
    # capitals_list = []
    # for capitals in capitals.values():
    #     capitals_list.append(capitals)
    # df = pd.DataFrame(capitals_list, columns = ['capitals'])
    # return df

    ###--- Loop over Dictionary Keys and Values ---###
    # df = pd.DataFrame(columns=['country', 'capital'])
    # row = 0
    # for country, capital in capitals.items():
    #     df.loc[row, ['country']] = country
    #     df.loc[row, ['capital']] = capital
    #     row += 1
    # return df


    ###--- Sets ---###
    # continents = {'America', 'Europe', 'Asia', 'Oceania', 'Africa', 'Africa'}
    # df = pd.DataFrame(continents, columns=['continents'])  
    # return df  