--Set Up table to show incremental refresh

{{
    config(
        materialized='table'
    )
}}
--base records

Select 
        '1' as ID, 
        'table' as Product,
        current_timestamp()::date - 2 as Order_Date,
        'Completed' as Ship_Status,
        current_timestamp()::date - 1 as Loaded_At

union all

Select 
        '2' as ID, 
        'desk' as Product,
        current_timestamp()::date - 2 as Order_Date,
        'Completed' as Ship_Status,
        current_timestamp()::date - 1 as Loaded_At

union all

Select 
        '3' as ID, 
        'chair' as Product,
        current_timestamp()::date - 1 as Order_Date,
        'In-Transit' as Ship_Status,
        current_timestamp()::date as Loaded_At


union all

Select 
        '4' as ID, 
        'Lamp' as Product,
        current_timestamp()::date - 1 as Order_Date,
        'In-Transit' as Ship_Status,
        current_timestamp()::date as Loaded_At

union all

Select 
        '3' as ID, 
        'chair' as Product,
        current_timestamp()::date - 1 as Order_Date,
        'Completed' as Ship_Status,
        current_timestamp()::date + 1 as Loaded_At
