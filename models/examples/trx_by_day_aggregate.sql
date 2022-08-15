{{
    config(
        materialized='view'
    )
}}

with trx as (
    Select *
    from {{ source('transaction_seed', 'transactions') }}
)

Select Date, sum(Revenue) as Daily_Revenue
from trx
group by 1
