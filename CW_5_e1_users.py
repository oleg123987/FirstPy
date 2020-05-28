"""
Из файла e1_users - users.csv получить список стран. Сохранить список в файл.
Вывести список в консоль. Раскрасить строки случайными цветами.
"""

from termcolor import cprint, colored


file_name = input(colored('Укажите имя файла: ', color='magenta'))
cprint('Argentina', color='cyan')

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