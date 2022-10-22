Select 
    loan_number as Ops_Loan_Number,
    Sales_Loan_Number,
    to_timestamp(First_Observed_Time) as First_Observed_Time,
    to_timestamp(Data_Warehouse_Load_Date) as Data_Warehouse_Load_Date 


from {{ source('hp', 'hp_ops') }}