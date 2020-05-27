# 18 тест
lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')

# 19 тест

lst = [2 ** x for x in range(0, 11)]
print(lst[-1])
# 20 тест
lst1 = '12,34'
lst2 = lst1.split(',')
print(type(lst1))
print(type(lst2))
# print(len(lst1)) < len(lst2)

# 21 тест

def fun(a, b=0, c=5, d=1):
    return a ** b ** c
print(fun(b=2, a=2, c=3))
# 2 ** 2 ** 3(или 4) ??? так работает?

# 22 тест

x = 5
f = lambda x: 1 + 2
print(f(x))

# 23 тест

# from math import pi as xyz
# print(pi)
