from random import shuffle
print(20*'-')
print('EMBARALHADOR DE NOMES')
print(20*'-')
print('digite os nomes a serem sorteados!')
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
lista = [a1, a2, a3, a4]
print('a ordem da apresentação será: {}'.format(shuffle(lista)))
