
file = open('resources/requirements.txt')

unique = set()  # создаем "множества" set, видимо присваиваем ему новый объект unique, скорее всего что-то из ООП
all = []  # создаем пустой массив all
for line in file.readlines():  # читаем файл по строкам
    value = line.strip()  # удаляем лишние символы и пробелы у строчки слева и справа
    unique.add(value)  # возвращаем в функцию unique , проверяем уникальность через set() и добавляем в unique
    all.append(value)  # добавляем все строчки

print(len(unique))  # считаем кол-во строк в unique (уникальные)
print(len(all))  # считаем кол-во всех строк

print('\n'.join(unique))  # преобразуем unique массив в строчки с переносом