select
    o.id as order_id
    , o.user_id as user_id
    , c.first_name
    , c.last_name
    , o.order_date
    , o.status as status_order

from {{ ref('stg__jaffle_shop_orders') }} as o
join {{ ref('stg__jaffle_shop_customers') }} as c
on o.user_id = c.id