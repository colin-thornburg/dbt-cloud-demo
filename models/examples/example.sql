Select * 
    from {{ ref('dim_customers') }}
    where customer_id is not null