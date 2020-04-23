# Посчитать в предложении количество гласных букв.


f = open(r'C:\Users\Oleg\PycharmProjects\First\resources\sentence.txt', encoding="utf-8")  # r - raw string
text = f.readline().lower()
f.close()

sum_vowels = (text.count('е')
              + text.count('и')
              + text.count('а')
              + text.count('ю')
              + text.count('я')
              + text.count('о'))
print(sum_vowels)


# print('а' == 'a')  # ru vs en
# print('hello \n word')
# print(r'hello \n word')
