import random
print(20*'=')
print('SORTEIO DE ALUNOS')
print(20*'=')
print('digite o nome dos alunos à serem sorteados')
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
p = a1, a2, a3, a4
s = random.sample(p, k=4)
print('a ordem da apresentação dos alunos será: ', s)
