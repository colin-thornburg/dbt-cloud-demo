with x as (

    select * from {{ ref('all_loan_records') }}
),

build_original_loan_num as (

Select 
iff(Sales_Loan_Number is not null, Sales_Loan_Number, iff(Ops_Loan_Number is not null, Ops_Loan_Number, Svc_Loan_Number))
as orig_loan_num

,* 
from x),

count_recs as (

Select 
    *, 
    count(surr_key) over (partition by orig_loan_num order by orig_loan_num, first_observed_time) as ct  
    
from build_original_loan_num
)

Select orig_loan_num, data_warehouse_load_date, Sales_Loan_Number, Ops_Loan_Number, Svc_Loan_Number from count_recs
where ct > 1