select
    id as payment_id,
    order_ID,
    payment_method,
    state as status,

    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount,
    created as created_at

from {{ source('stripe', 'payment') }}