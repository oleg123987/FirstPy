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


logs = ['resources/logs/statHrefs.log', 'resources/logs/statSearchHrefs.log']
# TODO как получить список файлов директории в Python

# summa = 0
# for path in logs:
#     summa += count_sum(path)
# print(summa)

print(sum(map(count_sum, logs)))

