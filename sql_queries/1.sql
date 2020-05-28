--1. Выгрузите имена, фамилии и адреса электронной почты 5 пользователей, сделавших больше всего заказов.
select first_name, last_name, email, count(order_sum) as orders_count, sum(order_sum) as total from `intense-wavelet-274110.DZ1.users` users
join `intense-wavelet-274110.DZ1.orders` orders on users.id = orders.user_id
group by users.first_name, users.last_name, users.email
order by orders_count desc
limit 5