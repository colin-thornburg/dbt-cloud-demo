--> Singular Test 
--> The test is applied to the stg_payments model to test that all amounts have a positive value
--> If the result of the query returns any results, the test fails

select
  order_id,
	sum(amount) as total_amount
from {{ ref('stg_payments') }}
group by order_id
having total_amount < 0