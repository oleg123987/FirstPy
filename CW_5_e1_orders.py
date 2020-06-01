#  Подсчитать общую сумму всех заказов
f_orders = open('resources/e1_orders - orders.csv')
f_orders.readline()  # пропуск первой строки с метаданными таблицы
summa = 0
for line in f_orders.readlines():
    summa += int(line.split(',')[-1])
f_orders.close()
print(summa)


with open('resources/e1_orders - orders.csv') as f_orders:
    next(f_orders)  # пропуск первой строки с метаданными таблицы
    total = sum([int(line.split(',')[-1]) for line in f_orders.readlines()])

print(total)
