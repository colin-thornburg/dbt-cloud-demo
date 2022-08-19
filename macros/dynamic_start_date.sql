{% macro start_date() %}
    {% set get_drop_commands_query %}
        Select '2018-01-01'as start
    {% endset %}
{% endmacro %}