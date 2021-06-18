import math
print(20*'=')
print('VALOR DA HIPOTENUSA')
print(20*'=')
co = float(input('digite o valor do cateto opostro: '))
ca = float(input('digite o valor do cateto adjacente: '))
print('sabendo que o cateto oposto é {} e o cateto adjacente é {}\ntemos a hipotenusa igual à {:.1f}'
      .format(co, ca, math.sqrt(co + ca)))
