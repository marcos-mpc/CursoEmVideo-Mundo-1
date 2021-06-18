print(20*'-')
print('DESFASENDO NUMEROS')
print(20*'-')
numero = input('digite um numero de entre 0 e 9999:')
unidade = numero.strip()[3]
dezena = numero.strip()[2]
centena = numero.strip()[1]
milhar = numero.strip()[0]
print('unidade = {}'.format(unidade))
print('dezena = {}'.format(dezena))
print('centena = {}'.format(centena))
print('milhar = {}'.format(milhar))
