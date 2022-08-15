{{
    config(
        materialized='table',
        tags=["transactions"]
    )
}}

Select * from {{ source('transactions', 'transactions') }}