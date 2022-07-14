--OBT for BI Tool

with customers as (
    Select * from {{ ref('dim_customers') }}
),

orders as (
    Select * from {{ ref('fct_orders') }}
),

final as (

    select
        orders.order_id,
        orders.customer_id,
        customers.first_name,
        customers.last_name,
        customers.number_of_orders,
        orders.order_date

    from orders
    left join customers using (customer_id)
)

Select * from final