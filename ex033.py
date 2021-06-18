print(30*'=')
print('MAIOR OU NENOR')
print(30*'=')
n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))
if n1 > n2 and n1 > n3:
    print('o {} é o maior numero!'.format(n1))
else:
    print('o {} é o menor numero!'.format(n1))
if n2 > n1 and n2 >n3:
    print('o {} é o maior numero!'.format(n2))
else:
    print('o {} é o menor numero!'.format(n2))
if n3 > n1 and n3 > n2:
    print('o maior numero é o {}!'.format(n3))
else:
    print('o menor numero é o {}!'.format(n3))
