# С помощью встроенной в Python библиотеки datetime узнать системное время.
# На основе этой информации выводить пользователю сообщение:
# Добрый вечер/день/ночи в зависимости времени суток
import datetime
a = datetime.datetime.now()
# a = datetime.date.today()
# print(a.year)
# print(a.month)
# print(a.day)
print(a.hour)
# print(a.minute)
# print(a.second)
if 18 <= a.hour <= 23:
    print('Добрый вечер')
if 0 <= a.hour <= 6:
    print('Доброй ночи')
if 6 < a.hour < 12:
    print('Доброе утро')
if 12 < a.hour < 18:
    print('Добрый день')

