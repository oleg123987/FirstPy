# Если сумма товаров в корзине пользователя больше или равна 3000, то применить скидку 30%.
# В ответ вывести итоговую сумму.

goods = ['1000', '20', '310', '2300']  # TODO данные сохранить в purchase.csv и читать их из этого файла

s = sum(int(goods[i]) for i in range(0, int(len(goods))))
s = sum(map(int, goods))


goods = [1000, 20, 310, 2300]
s = sum(goods)  # TODO расчёт скидки вынести в отдельный метод (см пример в 2_1)
if s >= 3000:
    print('Итоговая сумма со скидкой:', round(s * 0.7))
