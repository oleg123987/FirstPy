# Нужно определить, сдал ли студент экзамен?
# При количестве верных ответов 10 из 15 – сдал, если меньше – не сдал.
# Данные о кол-ве верных ответов получать от пользователя из консоли.
a = int(input('Введите количество верных ответов: '))

if 10 <= a <= 15:
    print('Сдал')
elif a > 15 or 0 > a:
    print('Не верное число')
else:
    print('Не сдал')

# Если сумма товаров в корзине пользователя больше или равна 3000, то применить скидку 30%.
# В ответ вывести итоговую сумму.

goods = [1000, 20, 300, 2000]

sum = (sum((int(goods[i]) for i in range(0, int(len(goods))))))
if sum > 3000:
    discount = sum - (float(0.30) * sum)
print('Итоговая сумма со скидкой:', discount)
