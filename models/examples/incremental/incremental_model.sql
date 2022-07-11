{{
    config(
        materialized='incremental',
        unique_key='id',
        on_schema_change='fail' 
    )
}}

Select * from {{ ref('incremental_source_table') }}

{% if is_incremental() %}
    -- this filter will only be applied on an incremental run
    where event_time > (select max(event_time) from {{ this }}) 
{% endif %}