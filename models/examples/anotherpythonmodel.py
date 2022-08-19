def add_one(x):
    return x + 1

def model(dbt, session):
    dbt.config(materialized="table")
    temps_df = dbt.ref("temperatures")
    
    # warm things up just a little
    df = temps_df.withColumn("degree_plus_one", add_one(temps_df["degree"]))
    return df