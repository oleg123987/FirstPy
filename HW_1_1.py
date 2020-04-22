# Даны две переменные с произвольными значениями. Поменять местами значения этих переменных.

a = 10
b = 20
print('a =', a, 'b =', b)
buf = a
a = b
b = buf
print('a =', a, ' b=', b)
print(b)
buf = a, b
print(buf, type(buf))
a = buf[1]
b = buf[0]
print('a =', a, 'b =', b)
a, b = b, a
print('a =', a, 'b =', b)
