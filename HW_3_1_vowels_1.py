# Посчитать в предложениях количество гласных букв
ru = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
en = ['a', 'i', 'u', 'e', 'o', 'y']

f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding='utf-8')
vowels_counter_en = 0
vowels_counter_ru = 0
for line in f.readlines():  # построчное чтение из файла
    line = line.lower()
    for letter in line:  # цикл по буквам в строке
        if letter in en:
            vowels_counter_en += 1
        if letter in ru:
            vowels_counter_ru += 1
f.close()
print('Количество гласных eng и ru всех строчек в файле:', vowels_counter_ru + vowels_counter_en)
print('Среди которых ru:', vowels_counter_ru)
print('Среди которых en:', vowels_counter_en)
