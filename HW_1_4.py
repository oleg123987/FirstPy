# Вычислите сумму элементов списка (=массива)

temperatures = [1, -2, -6, 17, 18, 24]

print('sum', sum(temperatures), sep='=')
print('sum =', sum(temperatures))
s = 0
for t in temperatures:
    if t > 0:
        s = s + t
        # print(t, s)
print('Сумма всех положительных чисел:', s)

t2 = []
for t in temperatures:
    if t > 0:
        t2.append(t)
print(t2)

for t in temperatures.copy():
    if t < 0:
        temperatures.remove(t)
print(temperatures)