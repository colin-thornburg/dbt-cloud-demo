--Snowflake supports merge statements.  delete+insert is optional config as this is default

{{
    config(
        materialized='incremental',
        unique_key=['id', 'order_date'],
        on_schema_change='append_new_columns', 
        incremental_strategy='delete+insert'
    )
}}

Select * from {{ ref('incremental_source_table') }}

{% if is_incremental() %}

    -- these filters will only be applied on an incremental run --> ignored on Full refresh
    where Loaded_At > (select max(Loaded_At) from {{ this }} ) 

{% endif %}