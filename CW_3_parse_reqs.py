
file = open('resources/requirements.txt')

unique = set()
all = []
for line in file.readlines():
    value = line.strip()
    unique.add(value)
    all.append(value)

print(len(unique))
print(len(all))

print('\n'.join(unique))