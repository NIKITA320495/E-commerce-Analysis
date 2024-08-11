# cumulative sales
select years, months ,payment,  sum(payment) over( order by years, months )  as cumulative_sales from
(select year(o.order_purchase_timestamp) as years ,month(o.order_purchase_timestamp) as months , round(sum(p.payment_value) ,2) as payment
from orders o join payments p on o.order_id=p.order_id
group by years , months ) as a
