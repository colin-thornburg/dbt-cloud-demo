{{
    config(
        materialized='table',
        tags=["transactions"]
    )
}}

Select * from {{ source('transaction_seed', 'transactions') }}