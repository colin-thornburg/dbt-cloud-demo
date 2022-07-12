--> Singular Test 
--> If the result of the query returns any results, the test fails

select
  customer_id,
	sum(number_of_orders) as orders
from {{ ref('demo_example') }}
group by customer_id
having orders < 0