-- Сколько в базе пользователей, не сделавших ни одной покупки?
select count(*) from `intense-wavelet-274110.DZ1.users` users
left join `intense-wavelet-274110.DZ1.orders` orders on users.id = orders.user_id
where orders.user_id IS NULL
