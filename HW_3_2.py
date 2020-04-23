# Посчитать общее количество слов в файле


f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding="utf-8")
text = f.readline().lower()  # TODO помнить, что в файле может быть несколько строк и нужно прочитать их всех
f.close()

words_amount = 0

# TODO здесь реализовать подсчёт

print(words_amount)
