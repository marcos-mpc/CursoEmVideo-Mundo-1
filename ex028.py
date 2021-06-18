from random import randint
print(20*'=')
print('JOGO DE ADIVINHAÇÃO')
print(20*'=')
n = randint(0, 5)
print('pensei em um numero entre 0 e 5...')
num = int(input('qual numero eu pensei ? '))
if num == n:
    print('PARABENS! vc acertou')
else:
    print('que pena, vc nao acertou. eu pensei em {} em vez de {}'.format(n, num))
