# Если сумма товаров в корзине пользователя больше или равна 3000, то применить скидку 30%.
# В ответ вывести итоговую сумму.

# goods = ['1000', '20', '310', '2300']
goods_csv = []

f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\goods.csv', encoding='utf-8')
for line in f.readlines():  # построчное чтение из файла
    print(line)
    goods_csv.append(line)
        # .replace("\n", "")

    # line = line.lower()
    # for letter in line:
print(goods_csv)
goods_csv = [line.rstrip() for line in goods_csv]
print(goods_csv)
f.close()

def price_goods(prices):
    total = sum(map(int, prices))
    discount_message = 'без скидки:'
    if total >= 3000:
        total *= 0.7
        discount_message = 'со скидкой:'
    print('Итоговая сумма', discount_message, round(total))
    return total


# s = sum(int(goods[i]) for i in range(0, int(len(goods))))

# price_goods(input().split())
res = price_goods(goods_csv)
# print(res)
# print(price_goods(['1000', '20', '310']))
