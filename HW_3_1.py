# Посчитать общее количество слов в файле


f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding="utf-8")  # r - raw string
text = f.readline().lower()
f.close()

sum_vowels = 0

# TODO здесь цикл и подсчёт гласных с его помощью

print(sum_vowels)


# TODO добавить все возможные гласные буквы русского алфавита в массив ru
# TODO добавить все возможные гласные буквы английского алфавита в массив en
# TODO реализовать подсчёт всех гласных букв через цикл по элементам массива ru
# TODO считать из файла вторую строку и реализовать ту же самую логику, только для массива en