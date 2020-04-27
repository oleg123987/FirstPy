# Посчитать общее количество слов в файле


f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding="utf-8")
# text = f.readline().lower()  # TODO помнить, что в файле может быть несколько строк и нужно прочитать их всех
words_amount = 0
line = f.readline()
while line:
    words_amount += len(line.split())
    line = f.readline()
print(words_amount)
f.close()




