# Если сумма товаров в корзине пользователя больше или равна 3000, то применить скидку 30%.
# В ответ вывести итоговую сумму.


def price_goods(prices):
    total = sum(map(int, prices))
    discount_message = 'без скидки:'
    if total >= 3000:
        total *= 0.7
        discount_message = 'со скидкой:'
    print('Итоговая сумма', discount_message, round(total))
    return total


f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\goods.csv', encoding='utf-8')

goods_csv = [line.rstrip() for line in f.readlines()]  # построчное чтение из файла
f.close()
print(goods_csv)
res = price_goods(goods_csv)


# s = sum(int(goods[i]) for i in range(0, int(len(goods))))
# goods = ['1000', '20', '310', '2300']
# price_goods(input().split())
# print(res)
# print(price_goods(['1000', '20', '310']))
