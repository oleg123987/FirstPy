
file = open('resources/requirements.txt')

unuqie = set()
all = []
for line in file.readlines():
    value = line.strip()
    unuqie.add(value)
    all.append(value)

print(len(unuqie))
print(len(all))

print('\n'.join(unuqie))