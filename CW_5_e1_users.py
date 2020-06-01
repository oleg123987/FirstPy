"""
Из файла e1_users - users.csv получить список стран. Сохранить список в файл.
Вывести список в консоль. Раскрасить строки случайными цветами.
"""
import random

from termcolor import cprint, colored

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

f_orders = open('resources/e1_users - users.csv')
f_orders.readline()  # пропуск первой строки с метаданными таблицы
countries = set()
for line in f_orders.readlines():
    countries.add(line.split(',')[6].strip())

f_orders.close()

for country in countries:
    index = random.randrange(0, len(colours))
    cprint(country, color=colours[index])

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
