--Snowflake supports merge statements.  delete+insert is optional config as this is default

{{
    config(
        materialized='incremental',
        unique_key='id',
        on_schema_change='append_new_columns', 
        incremental_strategy='delete+insert'
    )
}}

with a as (

    Select id, max(Loaded_At) as Max_Load_Date 
    from {{ ref('incremental_source_table') }} 
    group by id

), b as (

    Select * 
    from {{ ref('incremental_source_table') }} 
        )

Select 

    b.id, 
    b.product, 
    b.order_date, 
    b.ship_status, 
    b.Loaded_At 
    from b
    inner join a 
        on a.id = b.id and a.Max_Load_Date = b.Loaded_At

    {% if is_incremental() %}
    -- these filters will only be applied on an incremental run --> ignored on Full refresh
    where Loaded_At > (select max(Loaded_At) from {{ this }} ) 
    {% endif %}