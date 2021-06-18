num = int(input('digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {}...'.format(num))
print('unidade = {}\ndesena = {}\ncentena = {}\nmilhar = {}'.format(u, d, c, m))
