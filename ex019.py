from random import choice
print(20*'-')
print('SORTEIO DE ALUNOS')
print(20*'-')
print('DIGITE O NOME DOS ALUNOS À SEREM SORTEADOS.')
print(20*'-')
a1 = input('primeiro aluno: ')
a2 = input("segundo aluno: ")
a3 = input('terceiro aluno: ')
a4 = input('quatro aluno: ')
alunos = a1, a2, a3, a4
sorteio = choice(alunos)
print('o aluno sorteado para apagar o quadro foi o aluno {}'.format(sorteio))
