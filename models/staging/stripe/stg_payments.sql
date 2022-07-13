select
    id as payment_id,
    order_ID,
    payment_method,
    state as status,

    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount_USD,
    created as created_at

from {{ source('stripe', 'payment') }}