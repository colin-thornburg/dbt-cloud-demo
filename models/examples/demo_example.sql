
Select * from {{ ref('stg_orders') }}

where customer_id = 1