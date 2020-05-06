import string

# Посчитать в предложениях количество гласных букв
ru = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
en = ['a', 'i', 'u', 'e', 'o', 'y']

f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding='utf-8')
odd_letters = 0
for line in f.readlines():  # построчное чтение из файла
    for word in line.split():  # цикл по словам в строке
        # из слова удаляем лишние сиволы (не буквы), приводим к нижнему регистру, учитываем случай для "-" внутри слова
        word = word.strip(string.punctuation + string.whitespace).lower().replace('-', '')
        # если слово состоит из букв и не содержится в исключениях (массивы ru, en)
        print(word)
        for c in word:
            if c.contains(ru):
                odd_letters += 1
    # if word.isalpha() and word not in ru + en:
        #     words_amount += 1

f.close()
print('Количество гласных eng и ru всех строчек в файле:', odd_letters)

# TODO здесь цикл и подсчёт гласных с его помощью



# TODO добавить все возможные гласные буквы русского алфавита в массив ru



# TODO добавить все возможные гласные буквы английского алфавита в массив en



# TODO реализовать подсчёт всех гласных букв через цикл по элементам массива ru

# TODO считать из файла вторую строку и реализовать ту же самую логику, только для массива en