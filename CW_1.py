from statistics import mean

array = list(map(int, input('Введите 3 числа: ').split()))
# map - функция, применяющая другую функцию (название которой указывается в первом аргументе) к набору данных

s = sum(array)
composition = array[0] * array[1] * array[2]
arithmetic_mean = s / len(array)
arithmetic_mean1 = mean(array)

print('Сумма:', s)
print('Сумма: ' + str(s))  # так не надо, код читается хуже
print('Произведение:', composition)
print('Среднее арифметическое:{0:.2f}'.format(arithmetic_mean))
print('Среднее арифметическое:{0:.2f}'.format(arithmetic_mean1))

'''
line = input('Введите 3 числа:')  # ввод данных одной строкой
print(line)
array = line.split()
print(array)

for i in range(len(array)):  # преобразование элементов массива к числам
    array[i] = int(array[i])

print(array)
print(sum(array))
'''
