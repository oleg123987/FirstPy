select count(*) as orders_count, sum(order_sum) as total from `intense-wavelet-274110.DZ1.orders`
where user_id = 13175
--order by order_sum desc
--limit 3