Select * from raw.jaffleshop.orders

/*   Command: dbt run is executed ...

create or replace  view COLINT_DEMO.dbt_cthornburg.orders 

as (
Select * from raw.jaffleshop.orders
);

*/

--Command
-- dbt run --select model ex_stg_orders


