-- Сколько в базе заказов, для которых отсутствуют записи о пользователях?
select users.email, orders.orders_id from `intense-wavelet-274110.DZ1.users` users
right join `intense-wavelet-274110.DZ1.orders` orders on users.id = orders.user_id
where users.email IS NULL