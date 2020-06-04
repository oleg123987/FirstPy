select count(*) as orders_count, sum(order_sum) as total from `intense-wavelet-274110.DZ1.orders`
where user_id = 13175
--order by order_sum desc
--limit 3

-- Количество заказов по каждому email
select users.email, count(orders.orders_id) as orders_amount from `intense-wavelet-274110.DZ1.users` users
right join `intense-wavelet-274110.DZ1.orders` orders on users.id = orders.user_id
group by users.email