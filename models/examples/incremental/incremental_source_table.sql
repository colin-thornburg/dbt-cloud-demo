--Set Up table to show incremental refresh

{{
    config(
        materialized='table'
    )
}}
--base records

Select '1' as ID, to_date('2022.07.07 11:15:00', 'YYYY.MM.DD HH:MI:SS') as event_time
union all 
Select '2' as ID, to_date('2022.07.07 11:25:00', 'YYYY.MM.DD HH:MI:SS') as event_time