{{
    config(
        materialized='incremental'
    )
}}

with all_system_data as (

    {{ dbt_utils.union_relations(
        relations=[ref('stg_Sales'), ref('stg_Ops'), ref('stg_svc')]
    ) }}

)

Select 
    *, 
    {{ dbt_utils.surrogate_key(['Sales_Loan_Number', 'Ops_Loan_Number','svc_loan_number']) }} as Surr_Key

    
from all_system_data

{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  where data_warehouse_load_date > (select max(data_warehouse_load_date) from {{ this }})

{% endif %}
