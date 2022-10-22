select 
    loan_number as Sales_Loan_Number, 
    to_timestamp(First_Observed_Time) as First_Observed_Time, 
    to_timestamp(Data_Warehouse_Load_date) as Data_Warehouse_Load_date 


from {{ source('hp', 'hp_sales') }}