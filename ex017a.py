from math import hypot
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hi = hypot(co, ca)
print('o valor da hipotenusa é {:.2f}'.format(hi))
