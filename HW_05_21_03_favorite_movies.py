#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
print(my_favorite_movies[0:10])
#   последний
print(my_favorite_movies[-15:])
#   второй
print(my_favorite_movies[12:25])
#   второй с конца
print(my_favorite_movies[-22:-17])
# print(my_favorite_movies[35:40])

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

print(*my_favorite_movies.split(', '))
print(my_favorite_movies.find('Чужие'))  # возвращает индекс, с которого объект встретился в строке первый раз
# print(my_favorite_movies.replace(',', ':'))