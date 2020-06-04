# Узнайте, какая страна принесла больше денег, Россия или Бразилия?

russia = 'Russia'
brazil = 'Brazil'

ids_russia = list()
ids_brazil = list()

# получть ids пользователей из нужных стран
f_users = open('resources/e1_users - users.csv')
countries = set()
for line in f_users:
    row = line.strip().split(',')
    id, country = row[0], row[-1]
    if country == russia:
        ids_russia.append(id)
    if country == brazil:
        ids_brazil.append(id)
f_users.close()


def get_order_sum(user_id, ids, order_sum=0):  # TODO refactor
    if user_id in ids:
        order_sum = int(order_sum)
    return int(order_sum)


total_sum_ru = 0
total_sum_br = 0

f_orders = open('resources/e1_orders - orders.csv')
f_orders.readline()  # пропуск первой строки с метаданными таблицы
for line in f_orders:
    row = line.strip().split(',')
    user_id = row[0]
    order_sum = row[-1]
    total_sum_ru += get_order_sum(user_id, ids_russia, order_sum)
    total_sum_br += get_order_sum(user_id, ids_brazil, order_sum)
f_orders.close()

print(russia, total_sum_ru)
print(brazil, total_sum_br)

if total_sum_ru > total_sum_br:
    print(russia, end=' ')
elif total_sum_ru < total_sum_br:
    print(brazil, end=' ')
print('brought more money')