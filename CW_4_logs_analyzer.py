# в файлах statHrefs.log и statSearchHrefs.log выгружены логи с сервера приложения парсера веб-сайтов о недвижимости
# Нужно посчитать, сколько всего парсер обошёл страниц


file = open('resources/statHrefs.log')
summa = 0
amounts = []
for line in file.readlines():
    summa += int(line.split()[8])
    amounts.append(int(line.split()[8]))
file.close()

print(summa)
print(sum(amounts))
print(len(amounts))
print(amounts[:10])