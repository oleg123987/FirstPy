# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)  # множество - хранит только уникальные значения
meadow_set = set(meadow)

print('Виды цветов в саду', garden_set)
print('Виды цветов на лугу', meadow_set)

# выведите на консоль все виды цветов
print('Все виды цветов', garden_set | meadow_set)
output = garden_set.union(garden_set, meadow_set)
print('Все виды цветов', output)

# выведите на консоль те, которые растут и там и там
all_flowers = garden_set.intersection(meadow_set)
print('Растут там и там', all_flowers)
print('Растут там и там', garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
diff_set = garden_set.difference(meadow_set)
print('Не растут на лугу', diff_set)
print('Не растут на лугу', garden_set - meadow_set)

# symm_diff = garden_set.symmetric_difference(meadow_set)
# print(symm_diff)

# выведите на консоль те, которые растут на лугу, но не растут в саду

diff_set = meadow_set.difference(garden_set)
print('Не растут в саду', diff_set)
print('Не растут в саду', meadow_set - garden_set)

# symm_diff = meadow_set.symmetric_difference(garden_set)
# print(symm_diff)

# NOTE решение замечательное! Оформление шикарное! Спасибо за такой старательный подход