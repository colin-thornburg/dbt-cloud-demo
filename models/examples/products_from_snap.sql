{{
    config(
        materialized='table'
    )
}}
--base records

Select '1' as ID,'Popcorn' as Product, 2.75 as Price, current_date as updated_at
union all 
Select '2' as ID,'Candy' as Product, 3.50 as Price, to_date('2022.07.07 11:25:00', 'YYYY.MM.DD HH:MI:SS') as updated_at

--current_date