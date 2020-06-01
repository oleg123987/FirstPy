# TODO Узнайте, какая страна принесла больше денег, Россия или Бразилия?

f_users = open('resources/e1_users - users.csv')
f_users.readline()  # пропуск первой строки с метаданными таблицы
countries = set()
for line in f_users.readlines():
    pass
f_users.close()

f_orders = open('resources/e1_orders - orders.csv')
f_orders.readline()  # пропуск первой строки с метаданными таблицы
for line in f_orders.readlines():
    pass
f_orders.close()