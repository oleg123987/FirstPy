import string

# Посчитать общее количество слов в файле
ru = ['в', 'а', 'но']
en = ['a', 'the', 'at', 'and', 'of']

f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding='utf-8')
words_amount = 0
for line in f.readlines():  # построчное чтение из файла
    for word in line.split():  # цикл по словам в строке
        # из слова удаляем лишние сиволы (не буквы), приводим к нижнему регистру, учитываем случай для "-" внутри слова
        word = word.strip(string.punctuation + string.whitespace).lower().replace('-', '')
        # если слово состоит из букв и не содержится в исключениях (массивы ru, en)
        if word.isalpha() and word not in ru + en:
            words_amount += 1
f.close()
print('Sum of words:', words_amount)

