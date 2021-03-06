# Посчитать в предложениях количество гласных букв
ru = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
en = ['a', 'i', 'u', 'e', 'o', 'y']

vowels_ru = dict.fromkeys(ru, 0)
vowels_en = dict.fromkeys(en, 0)

f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding='utf-8')
for line in f.readlines():  # построчное чтение из файла
    line = line.lower()
    for vowel in ru:
        vowels_ru[vowel] += line.count(vowel)
    for vowel in en:
        vowels_en[vowel] += line.count(vowel)

f.close()

print(vowels_ru)
print(vowels_en)
sum_vowels_ru = sum(vowels_ru.values())
sum_vowels_en = sum(vowels_en.values())
print('Количество гласных eng и ru всех строчек в файле:', sum_vowels_ru + sum_vowels_en)
print('Среди которых ru:', sum_vowels_ru)
print('Среди которых en:', sum_vowels_en)

