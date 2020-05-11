
file = open('resources/requirements.txt')

unique = set()  # создаем пустое "множество" unique, присваиваем в unique пустой set
all = []  # создаем пустой массив all
for line in file.readlines():  # читаем файл по строкам
    # line = line.strip()  # удаляем лишние символы и пробелы у строчки слева и справа
    unique.add(line)  # добавляем в unique новое значение, проверяется уникальность через set()
    all.append(line)  # добавляем строку в массив all
file.close()
print(len(unique))  # считаем кол-во строк в unique (уникальные)
print(len(all))  # считаем кол-во всех строк
print(''.join(unique))  # преобразуем unique массив в строчки с переносом

file = open('resources/requirements_unique.txt', 'w+')
file.writelines(unique)
file.close()
