{% snapshot snap_products %}
    {{
        config(
            unique_key='id',
            strategy='timestamp',
            target_schema='snapshots',
            updated_at='updated_at'
        )
    }}

    select * from {{ ref('products_from_snap') }}
 {% endsnapshot %}