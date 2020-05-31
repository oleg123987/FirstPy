-- Узнайте, какая страна принесла больше денег, Россия или Бразилия?
select country, sum(order_sum) as orders_count from `intense-wavelet-274110.DZ1.users` users
join `intense-wavelet-274110.DZ1.orders` orders on users.id = orders.user_id
WHERE country="Russia" OR country="Brazil"
group by users.country
order by orders_count desc