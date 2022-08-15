{{
    config(
        materialized='view'
    )
}}

with trx as (
    Select *
    from {{ source('transactions', 'transactions') }}
)

Select Date, sum(Revenue) as Daily Revenue
from trx
group by 1
