from random import choice
from termcolor import cprint, colored

"""
Из файла e1_users - users.csv получить список стран. Сохранить список в файл.
Вывести список в консоль. Раскрасить строки случайными цветами.
"""

colours = [
    'grey',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white']

# file_name = input(colored('Укажите имя файла: ', color='magenta'))
# cprint('Argentina', color='cyan')

f_users = open('resources/e1_users - users.csv')
f_users.readline()  # пропуск первой строки с метаданными таблицы
countries = set()
# for line in f_users.readlines():
#     countries.add(line.split(',')[6].strip())
# решить с помощью генератора (то есть "заменить" цикл конструкцией в [])
[countries.add(line.split(',')[6].strip()) for line in f_users.readlines()]
f_users.close()

# for country in countries:
#     index = random.randrange(0, len(colours))
#     cprint(country, color=colours[index])
# пример решения с помощью генератора
[cprint(country, color=choice(colours)) for country in countries]

'''
Документация:
https://pypi.org/project/termcolor/
Примеры использования:
https://www.programcreek.com/python/example/78943/termcolor.colored

Чтобы эту библиотеку установить, нужно в консоли выполнить команду:
pip install termcolor

Или через настройки PyCharm: 
https://clck.ru/Ngn8D
'''
