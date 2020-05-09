import string
from pathlib import Path

# Посчитать в предложениях количество гласных букв
ru = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
en = ['a', 'i', 'u', 'e', 'o', 'y']

# f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding='utf-8')
f = open(Path(Path.cwd() / 'resources' / 'sentence.txt', encoding='utf-8'))
'''
Где почитать о pathlib:
https://habr.com/ru/post/453862
https://python-scripts.com/pathlib
'''

odd_letters = 0
for line in f.readlines():  # построчное чтение из файла
    for word in line.split():  # цикл по словам в строке
        # из слова удаляем лишние символы (не буквы), приводим к нижнему регистру, учитываем случай для "-" внутри слова
        word = word.strip(string.punctuation + string.whitespace).lower().replace('-', '')
        # если слово состоит из букв и не содержится в исключениях (массивы ru, en)
        for c in word:
            if c in ru:
                odd_letters += 1
        for c in word:
            if c in en:
                odd_letters += 1
    # if word.isalpha() and word not in ru + en:
        #     words_amount += 1

f.close()
print('Количество гласных eng и ru всех строчек в файле:', odd_letters)
