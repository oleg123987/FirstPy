# Если сумма товаров в корзине пользователя больше или равна 3000, то применить скидку 30%.
# В ответ вывести итоговую сумму.

goods = ['1000', '20', '310', '2300']

s = sum(int(goods[i]) for i in range(0, int(len(goods))))
s = sum(map(int, goods))


goods = [1000, 20, 310, 2300]
s = sum(goods)
if s >= 3000:
    print('Итоговая сумма со скидкой:', round(s * 0.7))