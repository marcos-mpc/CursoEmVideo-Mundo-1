from math import trunc
print(20*'-')
print('TRUNCANDO NUMEROS')
print(20*'-')
n = float(input('digite um numero real: '))
t = trunc(n)
print('o numero {} tem a parte inteira {}'.format(n, t))
