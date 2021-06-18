print(20*'-')
print('ALUGUEL DE CARRO')
print(20*'-')
d = int(input('digite a quantidade de dias que o carro foi alugado: '))
k = float(input('digite a quantidade de quilometros percorrido: '))
vk = k*0.15
vd = d*60
s = vk+vd
print('sabendo que foi percorrido {}km, e o carro foi alugado por {} dias o valor vai ficar por R${:.2f}'
      .format(k, d, s))
