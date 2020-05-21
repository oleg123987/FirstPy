# в файлах statHrefs.log и statSearchHrefs.log выгружены логи с сервера приложения парсера веб-сайтов о недвижимости
# Нужно посчитать, сколько всего парсер обошёл страниц


def count_sum(path):
    file = open(path)
    summa = 0
    # amounts = []
    for line in file.readlines():
        summa += int(line.split()[8])
        # amounts.append(int(line.split()[8]))
    file.close()

    # print(sum(amounts))
    return summa


file1 = count_sum('resources/logs/statHrefs.log')
file2 = count_sum('resources/logs/statSearchHrefs.log')
print(file1 + file2)