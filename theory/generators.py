lst = [i for i in range(0, 4)]
print(lst)

lst = []
for i in range(4):
    lst.append(i)

print(lst)
print(type(lst))  # list

keys = {i for i in range(0, 4)}
print(type(keys))  # set множество (только уникальные значения)

dct = dict()
dct.setdefault('key', 'hello')
print(type(dct))
print(dct)
